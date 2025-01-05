import pyttsx3

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.say(text) 
        engine.runAndWait()
    except:
        raise Exception("Can't read text out loud. Make sure you have given speaker access and installed all required packages.")