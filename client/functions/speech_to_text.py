import speech_recognition as sr
import pyttsx3 

def speech_to_text():
    r = sr.Recognizer() 

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            print("start talking")
            audio2 = r.listen(
                source,
                8,
                6,
            )

            print("recognizing audio")
            MyText = r.recognize_google(audio2)

            print(f"Did you say {MyText}")
            
    except sr.RequestError as e:
        print(f"Could not request results {e}")
        
    except sr.UnknownValueError:
        print("unknown error occurred")