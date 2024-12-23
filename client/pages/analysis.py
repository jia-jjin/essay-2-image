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