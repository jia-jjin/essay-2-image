import streamlit as st
import math
import pandas as pd
from functions.extractive import extractive
from functions.sentiment import sentiment
from functions.generate_image import generate_image
from functions.text_to_speech import text_to_speech
from functions.generate_prompt import generate_prompt

if "listened" not in st.session_state:
    st.session_state.listened = False
    
if "text" not in st.session_state:
    st.session_state.text = ""
    
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

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

    images_num = st.slider("Maximum number of images", 0, 3, 0)

    generator_type = st.radio(
        "Generator model",
        [
            "ZB-Tech/Text-to-Image",
            "black-forest-labs/FLUX.1-dev",
        ],
        captions=[
            "10~15s, 85% accurate",
            "30~40s, 95% accurate",
        ],
    )

    api_key = st.text_input(
        "Hugging Face API Key (please grant access to use FLUX.1-dev using link at the bottom)",
        st.session_state.api_key
    )
        
    link = "https://huggingface.co/black-forest-labs/FLUX.1-dev"
    st.markdown(
        f"<a style='display: block; text-align: start;' href={link}>Grant access</a>",
        unsafe_allow_html=True,
    )

    text = st.text_area(
        "Text to be summarized",
        st.session_state['text'],
        height=200
    )
    
    submit = st.form_submit_button('Submit')


if submit or st.session_state.listened:

    if not text:
        st.error("No text provided.")
        st.stop()
    
    f"Total word length: {len(text.split())}"

    st.session_state['api_key'] = api_key
    st.session_state['text'] = text

    try:
        if images_num > 0:
            st.write("## Images")
            imageRow = st.columns(3)
        
        if summarizer == 'Extractive':
            summary, sentenceValues = extractive(text, max_sentences, min_relevance)
                
        elif summarizer == 'Sentiment':
            summary, emotions, keywords = sentiment(text)

            _, sentenceValues = extractive(summary, 1000000)
            # if images_num > 0:
                
            #     images = generate_image(selected_sentences[:images_num], generator_type, api_key)
                
        col1, col2 = st.columns([3,1], vertical_alignment='bottom')
        st.write(summary)
        with col1:
            st.write("## Summarized text")
        with col2:
            if st.button("Listen 🔉", use_container_width=True, on_click=on_listen):
                text_to_speech(summary)

        if images_num > 0:
            sentenceValuesSorted = list(map(lambda x: x[0],sorted(sentenceValues.items(), reverse=True, key=lambda x: x[1])))
            image_prompts = [generate_prompt(sentence) for sentence in sentenceValuesSorted[:images_num]]
            images = generate_image(image_prompts, generator_type, api_key)
        for i in range(images_num):
            imageRow[i].image(images[i])

        if summarizer == 'Sentiment':
            st.write("## Overall emotions")
            for i in range(len(emotions)):
                st.write(f"{i+1}. {emotions[i]['label']} ({round(emotions[i]['score'] * 100, 2)}%)")
                
            st.write("## Top key words/phrases")
            for i in range(len(keywords)):
                st.write(f"{i+1}. {keywords[i]}")

    except Exception as e:
        st.error(e)
    except:
        st.error("Something went wrong")







