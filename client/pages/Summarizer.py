import streamlit as st
import pandas as pd
from functions.extractive import extractive
from functions.generate_image import generate_image

with st.form("main"):
    summarizer = st.radio(
        "Pick a summarizer type",
        ["Extractive", "Abstractive"],
    )

    images_num = st.slider("Number of images", 0, 3, 1)
    
    text = st.text_area(
        "Text to be summarized",
        height=200
    )
    
    submit = st.form_submit_button('Submit')


if submit:
    f"Total word length: {len(text.split())}"

    summary, sentenceValues = extractive(text)
    if images_num > 0:
        sentenceValuesSorted = list(map(lambda x: x[0],sorted(sentenceValues.items(), reverse=True, key=lambda x: x[1])))
        images = generate_image(sentenceValuesSorted[:images_num])
        st.write("## Images")
        imageRow = st.columns(3)
        for i in range(images_num):
            imageRow[i].image(images[i])
    
    st.write("## Summarized text")
    if summarizer == 'Extractive':
        st.write(summary)