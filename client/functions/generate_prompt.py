import torch
from transformers import T5Tokenizer 
import streamlit as st

@st.cache_data
def generate_prompt(sentence):
    @st.cache_resource
    def create_prompts(_model, _tokenizer, _device, input_text, max_length=128):
        model.eval()
    
        inputs = tokenizer(
            input_text,
            max_length=max_length,
            padding=True,
            truncation=True,
            return_tensors='pt'
        ).to(device)
        
        outputs = model.generate(
            input_ids=inputs['input_ids'],
            attention_mask=inputs['attention_mask'],
            max_length=max_length,
            temperature=0.8,  # Add some randomness
            do_sample=True,  # Enable sampling
        )
        
        generated_prompts = [
            tokenizer.decode(output, skip_special_tokens=True)
            for output in outputs
        ]
        
        return generated_prompts
    
    model = torch.load("models/prompt_generator_T5_v2")
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    
    generated_prompts = create_prompts(model, tokenizer, device, sentence)
    
    return generated_prompts[0]