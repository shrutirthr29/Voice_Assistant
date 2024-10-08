import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant ma'am. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_GMAIL_ACCOUNT', 'YOUR_PASSWORD')
    server.sendmail('YOUR_GMAIL_ACCOUNT', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            speak("Playing the song for you ma'am")
            music_dir = 'C:\\songs\\Favs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ma'am, the time is {strTime}")

        elif 'open code' in query:
            speak("opening code")
            codePath = "C:\\Users\\shrut\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "RECEIVER_GMAIL_ACCOUNT"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ma'am I am not able to send this email")    

        elif 'quit' or 'stop' or 'terminate' in query:
            speak("Okay Thankyou for coming here")
            exit()
