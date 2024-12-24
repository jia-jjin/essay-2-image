import streamlit as st
import numpy as np
import pandas as pd

raw_df = pd.read_csv('output/raw.csv')
df = pd.read_csv('output/cleaned.csv')

col1, col2 = st.columns(2)

with col1:
    st.write("### Raw Prompts", raw_df)
with col2:
    st.write("### Cleaned Prompts", df)

st.header("Wordcloud showing importance of words among prompts")
st.image("output/wordcloud.png")

st.header("Frequency distribution of words among prompts")
st.image("output/freqdist.png")

st.header('Documentation and Assumptions')
st.write("Based on the wordcloud and words' frequency distribution graph generated, we can see that most occured words are the ones that describe the image generated, e.g. art, potrait, detailed, painting, concept, artstation etc.")
st.write("This means that based on the sentence/essay we are going to summarize, we must add a few keywords that describes the image generated for it to fit the general theme better.")
st.write("E.g. art for cartoony images, potrait when there's only a few characters involved in the image, painting when it shows an event from the past.")