import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and return the text"""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except:
            speak("Sorry, I didn't catch that. Could you say it again?")
            return None
        return query.lower()

def greet_user():
    """Greet the user based on the time"""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you today?")

def tell_time():
    """Tell the current time"""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def search_wikipedia(query):
    """Search Wikipedia for the given query"""
    speak('Searching Wikipedia...')
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

if __name__ == "__main__":
    greet_user()
    
    while True:
        command = listen()

        if command:
            if 'time' in command:
                tell_time()
            elif 'wikipedia' in command:
                search_query = command.replace('wikipedia', '')
                search_wikipedia(search_query)
            elif 'exit' in command:
                speak("Goodbye!")
                break
