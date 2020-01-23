import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour <18:
        speak("Good Afternoon Alee")

    else :
        speak("Good Evening!")

    speak ("I am your Voice Assistant, Tell me How may I be of assistance")

def takeCommand():
    #it takes voice input and returns output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print('You said :{}'.format(query))
    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            #speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open google' in query:
            wb.open("google.com")

        elif 'open facebook' in query:
            wb.open("facebook.com")

        elif 'open github' in query:
            wb.open("github.com")

        elif 'open mail' in query:
            wb.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Alee Sir, The time is {strTime}")

        elif 'email to wajahat' in query:
            try:
                speak("Content, Sir?")
                content = takeCommand()
                to = "wajahatsaleem9@gmail.com"
                sendEmail(to, content)
                speak ("Sir, Email has been sent!")
            except Exception as e:
                print (e)
                speak("Apologies, The email has not been sent")

