import spacy
from transformers import pipeline
from rake_nltk import Rake
import streamlit as st

@st.cache_data
def sentiment(t):

    nlp = spacy.load("en_core_web_sm")
    
    t = t.replace('’', "'")
    doc = nlp(t)
    final_text = doc.text

    @st.cache_resource
    def discover_emotions(text):
        sentiment_analysis = pipeline("sentiment-analysis")
        return sentiment_analysis(text)

    @st.cache_data
    def extract_keywords(text):
        rake = Rake()
        rake.extract_keywords_from_text(text)
        return list({e:None for e in rake.get_ranked_phrases()}.keys())

    @st.cache_data
    def splitTextIntoChunks(text, chunk_size=1024):
      chunks = []
      for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
      return chunks

    @st.cache_resource
    def summarize(text, chunk_size=1024, chunk_summary_size=128):
      summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
      chunks = splitTextIntoChunks(text, chunk_size)
    
      summaries = []
      for chunk in chunks:
        size = chunk_summary_size
        if(len(chunk) < chunk_summary_size):
          size = len(chunk)/2
        summary = summarizer(chunk, min_length=1, max_length=size)[0]["summary_text"]
        summaries.append(summary)
    
      main_summary = ""
      for summary in summaries:
        main_summary += summary + " "
    
      return main_summary

    final_summary = summarize(final_text)

    return final_summary, discover_emotions(final_summary), extract_keywords(final_summary)