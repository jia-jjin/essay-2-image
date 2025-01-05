import streamlit as st
from functions.generate_prompt import generate_prompt
from nltk.tokenize import sent_tokenize

with st.form("main"):

    text = st.text_area(
        "Insert text to generate prompts (separate with full stop for multiple prompts)",
        height=200
    )
    
    submit = st.form_submit_button('Generate')

if submit:

    if not text:
        st.error("No text provided.")
        st.stop()
    
    f"Total word length: {len(text.split())}"

    try:
        sentences = sent_tokenize(text)
        image_prompts = [generate_prompt(sentence) for sentence in sentences]
        for i in range(len(image_prompts)):
            st.write(f"""
                {i+1}. 
                Original: {sentences[i]} \n\n
                Prompt: {image_prompts[i]}
            """)


    except Exception as e:
        st.error(e)
    except:
        st.error("Something went wrong")







