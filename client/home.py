import streamlit as st
import pandas as pd

summarizer = st.radio(
    "Pick a summarizer type",
    ["Extractive", "Abstractive"],
)

text = st.text_area(
    "Text to be summarized",
    height=200
)

f"Total word length: {len(text.split())}"