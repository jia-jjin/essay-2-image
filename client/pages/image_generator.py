import streamlit as st
from functions.generate_image import generate_image
    
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

with st.form("main"):

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

    text = st.text_input(
        "Insert text to generate images (recommended 1 sentence at max)",
    )
    
    submit = st.form_submit_button('Generate')


if submit:

    if not text:
        st.error("No text provided.")
        st.stop()
    
    st.session_state['api_key'] = api_key

    try:
        st.write("## Images")
        images = generate_image([text], generator_type, api_key)
        for i in range(len(images)):
            st.image(images[i])

    except Exception as e:
        st.error(e)
    except:
        st.error("Something went wrong")







