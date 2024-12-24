import streamlit as st
import pandas as pd
from functions.extractive import extractive
from functions.sentiment import sentiment
from functions.generate_image import generate_image
from functions.text_to_speech import text_to_speech

if "listened" not in st.session_state:
    st.session_state.listened = False

def on_listen():
    st.session_state.listened = True
    
def remove_listen():
    st.session_state.listened = False

summarizer = st.radio(
    "Pick a summarizer type",
    [
        "Sentiment", 
        "Extractive", 
    ],
    on_change=remove_listen
)

if summarizer == "Extractive":
    summary_type = st.radio(
        "Pick a summary type",
        [
            "Sentence relevance",
            "Sentence count",
        ]
    )
    
    max_sentences = None
    min_relevance = None
    if summary_type == "Sentence count":
        max_sentences = st.slider("Max number of sentences", 0, 20, 5)
    else:
        min_relevance = st.slider("Minimum relevance of sentences", 0.0, 2.0, 1.5)

with st.form("main"):

    images_num = st.slider("Number of images", 0, 3, 0)
    

    if st.session_state['text']:
        text = st.text_area(
            "Text to be summarized",
            st.session_state['text'],
            height=200
        )
    else:
        text = st.text_area(
            "Text to be summarized",
            height=200
        )
    
    submit = st.form_submit_button('Submit')


if submit or st.session_state.listened:
    f"Total word length: {len(text.split())}"

    st.session_state['text'] = text

    if summarizer == 'Extractive':
        summary, sentenceValues = extractive(text, max_sentences, min_relevance)
        if images_num > 0:
            sentenceValuesSorted = list(map(lambda x: x[0],sorted(sentenceValues.items(), reverse=True, key=lambda x: x[1])))
            images = generate_image(sentenceValuesSorted[:images_num])
            st.write("## Images")
            imageRow = st.columns(3)
            for i in range(images_num):
                imageRow[i].image(images[i])
        
    elif summarizer == 'Sentiment':
        summary, emotions, keywords = sentiment(text)
        
        st.write("## Overall emotions")
        for i in range(len(emotions)):
            st.write(f"{i+1}. {emotions[i]['label']} ({round(emotions[i]['score'] * 100, 2)}%)")
            
        st.write("## Top key words/phrases")
        for i in range(len(keywords[:10])):
            st.write(f"{i+1}. {keywords[i]}")
            
    col1, col2 = st.columns([3,1], vertical_alignment='bottom')
    st.write(summary)
    with col1:
        st.write("## Summarized text")
    with col2:
        if st.button("Listen 🔉", use_container_width=True, on_click=on_listen):
            text_to_speech(summary)
            








