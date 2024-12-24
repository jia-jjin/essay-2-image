import streamlit as st

st.write("# essay-2-image")
st.write("This machine learning project is mainly about translating words or essays into stunning and informational images aiming to serve as replacements or trigger points during presentations.")
st.image("output/example.png")

st.write("## Key metrics")

key_metrics = [
    {
        "title": "Image Quality",
        "content": "Let users evaluate how visually appealing and relevant the images are to the text."
    },
    {
        "title": "Feedback Rating",
        "content": "Users rate how well the images represent their content in presentations (relevance, informativeness, visual appeal)"
    },
    {
        "title": "System Efficiency",
        "content": "Measure how well the translation performs as input size increases."
    },
    {
        "title": "Audience Feedback",
        "content": "Evaluate whether the images help improve audience understanding or attention during presentations."
    },
    {
        "title": "Error Metrics",
        "content": "Measure how often the generated image gives off an incorrect meaning."
    },
]

for i in range(len(key_metrics)):
    st.write(f"##### {i+1}. {key_metrics[i]['title']}")
    st.write(key_metrics[i]['content'])

st.write("## Bottlenecks & Recommendations")
st.write("This application is currently facing a few bottlenecks, including not being able to produce a lot of images in a short period of time due to HuggingFace's constraints of API calls. The prompts translated from sentences may not be 100% accurate too, due to limitations and inaccuracies of converting prompts into sentences as training data for the model by GPT models.")
st.write("Some steps to be taken are to implement higher capacity GPUs to produce images locally instead of making API calls, and also increase speed of model training to increase accuracy of the model during translation of sentences into prompts.")