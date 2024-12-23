from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from time import sleep

def generate_image(prompts):
    
    load_dotenv()

    image_api_key = os.getenv("HUGGING_FACE_API")
    
    print("Your api key is " + image_api_key)
    
    client = InferenceClient("ZB-Tech/Text-to-Image", token=image_api_key)
    # client = InferenceClient("black-forest-labs/FLUX.1-dev", token=image_api_key)
    
    output = []
    
    for i in range(len(prompts)):
        output.append(client.text_to_image(prompts[i]))
        # if i < len(prompts) - 1:
        #     sleep(30)

    return output