import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclibrary
import requests
from groq import Groq

recognizer = sr.Recognizer()
newsapi = "64cadc86b81240e49f464a29ce272764"

def speak(text):
    print("Jarvis says:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def aiprocess(command):
        client = Groq(
        api_key="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"
        )

    # Send a chat completion request
        completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # free model
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud."},
            {"role": "user","content": command}
        ]
        )

# Print the assistant's response
        return completion.choices[0].message.content

def processCommand(c):
    # Placeholder for future commands
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif"chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linked1In" in c.lower():
        webbrowser.open("https://LinkedIn.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)


    else:
        #let openAI will handle this
       output = aiprocess(c)
       speak(output)

    
    
    

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    
    while True:
        # Listen for the wake word "Jarvis"
        r = sr.Recognizer() 

        print("recognizing..")  
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
                word = r.recognize_google(audio)
                if "jarvis" in word.lower():
                    speak("Ya")

                    # Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))