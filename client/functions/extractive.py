import nltk 
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize 
import streamlit as st

@st.cache_data
def extractive(text, max_sentences=None, min_relevance=None):
    stopWords = set(stopwords.words("english")) 
    words = word_tokenize(text) 
       
    freqTable = dict() 
    for word in words: 
        word = word.lower() 
        if word in stopWords or word in string.punctuation: 
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1
       
    sentences = sent_tokenize(text) 
    sentenceValue = dict() 
       
    for sentence in sentences: 
        for word, freq in freqTable.items(): 
            if word in sentence.lower(): 
                if sentence in sentenceValue: 
                    sentenceValue[sentence] += freq 
                else: 
                    sentenceValue[sentence] = freq 
       
    sumValues = 0
    for sentence in sentenceValue: 
        sumValues += sentenceValue[sentence] 
       
       
    summary = '' 
    if min_relevance != None:
        average = int(sumValues / len(sentenceValue)) 
        for sentence in sentences: 
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (min_relevance * average)): 
                summary += sentence + " "
    else:
        selectedSentences = list(map(lambda x: x[0],sorted(sentenceValue.items(), reverse=True, key=lambda x: x[1])))[:max_sentences]
        for sentence in sentences: 
            if (sentence in sentenceValue) and (sentence in selectedSentences): 
                summary += sentence + " "

    return summary, sentenceValue