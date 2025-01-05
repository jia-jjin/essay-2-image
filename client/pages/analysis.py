import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('data/cv-unique-has-end-punct-sentences.csv')
df2 = pd.read_csv('data/cleaned_training_data.csv')

col1, col2 = st.columns(2)

with col1:
    st.write("### Sentences (10k rows)", df)
with col2:
    st.write("### Cleaned Sentence and Image Prompt Pairs", df2)

st.header("Wordcloud showing importance of words among prompts")
st.image("output/prompts_wordcloud.png")

st.header("Frequency distribution of words among prompts")
st.image("output/prompts_freqdist.png")

st.header("Wordcloud showing importance of words among sentences")
st.image("output/sentences_wordcloud.png")

st.header("Frequency distribution of words among sentences")
st.image("output/sentences_freqdist.png")

st.header('Documentation and Assumptions')
st.write("As what I have observed, compared to the sentence column which has a total vocabulary richness of 43.62%, the prompts column unsurprisingly has less than 5% of vocabulary richness. This is probably due to the repetition in words used to describe the images. This means that as long as the model captures important keywords among the prompts, it can easily generate image prompts.")
st.write("For the task of converting sentences into image prompts, after doing intensive research, I have decided to try out GANs which generates sentences based on the hint or input given, and also Seq2Seq models which learn and detect patterns from one text sequence to another, which is definitely more applicable for this use case.")