import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voices', voices[0].id)
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.login("harshvaghani02@gmail.com", "C:\\Users\\LEGION\\Desktop\\password")
    server.sendmail("harshvaghani02@gmail.com", to, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("im jarvis sir please tell me how my i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recongnizing..")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print('say that again')
        return "None"
        return query

    if 'Wikipedia' in query:
        speak('searching wikipedia')
        query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("accourding to wikipedia")
        print(query)
        speak(results)
    elif 'wikipedia' in query:
        speak('searching wikipedia')
        query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("accourding to wikipedia")
        print(query)
        speak(results)
    elif 'please help me to get a girlfriend' in query:
        speak("nope hm it seems like noone likes you be single be with yourself fucking bustard idiot girl will not like your fucking face bitch dumb bitch hit your fucking face lodu")
    elif 'how to get a girlfriend' in query:
        speak("fuck you fucking idiot but i just want to tell you that it seems like you will never have girlfriend im also single ha ha ha ha ha fuck you bitch ")
    elif 'open YouTube' in query:
        webbrowser.open("https://www.youtube.com/")
    elif 'open Google' in query:
        webbrowser.open("https://www.google.com/")
    elif 'open carryminati' in query:
        webbrowser.open("https://www.youtube.com/user/AddictedA1")    
    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")    
    # elif 'play music' in query:
    #     music_dir = 'D:\\Songs'
    #     songs = os.listdir(music_dir)
    #     print(songs)
    #     os.startfile(os.path.join(music_dir, songs[1]))
    elif 'music' in query:
        music_dir = 'D:\\hm'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strtime("%H:%M:%S")
        speak(strTime)
    elif 'open code' in query:
        codepath = ""C:\Users\LEGION\AppData\Local\Programs\Microsoft VS Code\Code.exe""
        os.startfile(codepath)
    elif 'open my folder' in query:
        path = "E:\\"
        os.startfile(path)    
    elif 'email to Harsh' in query:
        try:
            speak("what should i send")
            content = takeCommand()
            to = "harshvaghani02@gmail.com"
            sendEmail(to, content)
            speak("Email has been send")
        except Exception as e:
            print(e)
            speak("sorry sir im not able to send this email")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()



    #         speak("nope hm it seems like noone likes you be single be with yourself fucking bustard idiot girl will not like your fucking face bitch dumb bitch hit your fucking face lodu")
    # elif 'open YouTube' in query:
    #     webbrowser.open("youtube.com")
    # elif 'open Google' in query:
    #     webbrowser.open("google.com")
    # elif 'open stack overflow' in query:
    #     webbrowser.open("stackoverflow.com")
    # elif 'play a music' in query:
    #     music_dir = 'D:\\Songs'
    #     songs = os.listdir(music_dir)
    #     print(songs)
    #     os.startfile(os.path.join(music_dir, songs[1]))
    # elif 'the time' in query:
    #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
    #     speak(f"sir the time is {strTime}")
    # elif 'open code' in query:
    #     codepath = "C:\\Users\LEGION\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    #     os.startfile(codepath)
    # elif 'email to Harsh' in query:
    #     try:
    #         speak("what should i send")
    #         content = takeCommand()
    #         to = "harshvaghani02@gmail.com"
    #         sendEmail(to, content)
    #         speak("Email has been send")
    #     except Exception as e:
    #         print(e)
    #         speak("sorry sir im not able to send this email")

