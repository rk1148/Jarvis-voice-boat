import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser
import os
import smtplib
import datetime 

# # Inilialize the recognizer from this speech recognition
listener = sr.Recognizer()
# #initilalize the pythontotextspeech
player = pyttsx3.init() #by this our system will be speak out

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  

    talk("I am Jarvis Sir. Please tell me how may I help you")


# #we are going to listen whatever voice we receive from the microphone
# #so first enable the microphone

# #step-1  It will take the voice and convert it into text
def listen():
    with sr.Microphone() as input_device:
        print("I am ready, Listening ....")
        listener.pause_threshold = 1
        voice_content = listener.listen(input_device)

    try:
        print("Recognizing...")     
        text_command = listener.recognize_google(voice_content)
        # text_command = text_command.lower()
        print(text_command)

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return text_command

# ##  ## step-2 text to speech convert
def talk(text):
    player.say(text)
    player.runAndWait()              #it will wait while our voice bot speaks out this statement

# we are using the SMTP module of python--> The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon. 
def sendEmail(to, content):
    # for this we have to enable less secure apps. Otherwise, the sendEmail function will not work properly.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()                   # ehlo() just tells the server that you're going to be sending a message through it.
    server.starttls()               # starttls() says that from now on, all the data sent will be sent through TLS, so all your passwords will be safe and encrypted.
    server.login('rajkhandelwal3152001@gmail.com','Ansh@1234') # email me login krne k lia
    server.sendmail('rajkhandelwal3152001@gmail.com',to, content)
    server.close()





if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        command = listen().lower()
        if "jarvis" in command:
            command = command.replace("jarvis","")

            if "what is" in command:
                command = command.replace("what is", "")
                info = wikipedia.summary(command, sentences=2)
                talk(info)
            elif "who is" in command:
                command = command.replace("who is", "")
                info = wikipedia.summary(command, 5)
                talk(info)

            elif "play" in command:
                command = command.replace("play", "")
                pywhatkit.playonyt(command)
            elif 'open youtube' in command:
                webbrowser.open("youtube.com")
            elif 'open google' in command:
                webbrowser.open("google.com") 
            elif 'the time' in command:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                talk(f"Sir, the time is {strTime}")
            # elif 'open code' in command:
            #     codePath = "C:\Users\Lenovo\anaconda3\Lib\site-packages\anaconda_navigator\static\images\logos"
            #     os.startfile(codePath)
            
            elif 'email to Raj' in command:
                try:
                    talk("What should I say?")
                    content = listen()
                    to = "rajkhandelwal3152001@gmail.com"    
                    sendEmail(to, content)
                    talk("Email has been sent!")
                except Exception as e:
                    print(e)
                    talk("Sorry sir. I am not able to send this email")    

            else:
                talk("Sorry, I am unable to find what you looking for")
    
                 



















































# Reference youtube vedio
# 1.    https://www.youtube.com/watch?v=Lp9Ftuq2sVI&ab_channel=CodeWithHarry
# 2.    https://www.youtube.com/watch?v=kJPigvW1HK4&t=1144s&ab_channel=DataMagic%28bySunnyKusawa%29