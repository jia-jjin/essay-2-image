from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from time import sleep
import streamlit as st

@st.cache_data
def generate_image(prompts, generator_type, image_api_key):
    
    # load_dotenv()

    # if not image_api_key:
    #     image_api_key = os.getenv("HUGGING_FACE_API")

    if not image_api_key:
        raise Exception("No API key provided to execute image generation.")

    client = InferenceClient(generator_type, token=image_api_key)
    
    output = []
    
    for i in range(len(prompts)):
        output.append(client.text_to_image(prompts[i]))
        # if i < len(prompts) - 1:
        #     sleep(30)

    return output