# essay-2-Image
This machine learning project translates words or essays into stunning and informational images, aiming to serve as replacements or trigger points during presentations.

## Introduction
Incorporating relevant visuals into presentations can significantly enhance audience engagement and understanding. This project leverages machine learning to automatically generate images and summaries based on users' preferences.

## Features
Text-to-Image Generation: Converts important sentences in generated summary into corresponding images.
Customizable Outputs: Allows adjustments to image and summarizing style based on user preferences.

## Installation

Clone the repository:
```bash
git clone https://github.com/jia-jjin/essay-2-image.git
cd essay-2-image
```

Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

Run Streamlit client:
```bash
streamlit run client/home.py
```

## Usage
1. Prepare your looooong text.
2. Navigate to the Summarizer page in the client.
3. Pick a summarizer type.
4. If you would like to use black-forest-labs/FLUX.1-dev, make sure to create a HuggingFace account and grant access to the model using this [link](https://huggingface.co/black-forest-labs/FLUX.1-dev).
5. Include your HuggingFace API key if you would like to use black-forest-labs/FLUX.1-dev to generate images.
6. Include your looooong text.
7. Click on the submit button and watch as the magic unfolds itself.

## Credits
- Thanks to GeeksForGeeks for their step-by-step guides
