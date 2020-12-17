import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good after noon")

    else:
        speak ("good evening")

    speak("i am mainul islam rajons personal assistant please tell me how can i help you ?")  
def takeCommand():
    #it takes microphone input abd returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening .....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        

        print("say that again")
        return "none"
    return query    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic fob executing tasks based on queary
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")    

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'love'  in query:
            
            speak("sabrina rahman ema is your love")
