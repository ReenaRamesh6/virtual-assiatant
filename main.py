import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
engine.say(audio)
engine.runAndWait()
defwishMe():
hour =datetime.datetime.now().hour
if0 <=hour<12:
speak("GoodMorning!")
elif 12<=hour<16:
speak("Goodafternoon!")
elif 16<=hour<19:
speak("Goodevening!")
else:
speak("Goodnight!")
speak("IamJarvis. TellmehowmayIhelpyou.")
deftakeCommand():
r =sr.Recognizer()
with sr.Microphone()assource:
print("Listening...")
r.pause_threshold=1
audio=r.listen(source)
try:
print("Recognizing...")
query=r.recognize_google(audio,language='en-in')
print(f"User said:{query}\n")
exceptExceptionase:
print("Saythat againplease...")
return"None"
returnquery
defsendEmail(to, content):
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('your_email@gmail.com','your_password')
server.sendmail('your_email@gmail.com',to,content)
server.close()
#IntentRecognitionModel
deftrain_intent_recognition_model():
# Sampledataset ofcommandsandintents
data ={
'command':[
"What'stheweatherlike?",
"Tellmeajoke.",
"Setatimerfor10minutes.",
"Playsomemusic.",
"Whattimeisit?",
"HowdoImake pancakes?",
"Tellmeastory.",
"What'sthenewstoday?",
"OpenYouTube",
"OpenGoogle",
"SendanemailtoPranay"
],
'intent': [
"weather",
"joke",
"timer",
"music",
"time",
"recipe",
"story",
"news",
"open_youtube",
"open_google",
"send_email"
]
}
# Createa DataFrame
df= pd.DataFrame(data)
# Splitthedata intotrainingandtestingsets
X_train,X_test, y_train, y_test=train_test_split(df['command'],df['intent'],
test_size=0.2, random_state=42)
# Createa pipelinethatcombinesTF-IDFandNaiveBayes
model= make_pipeline(TfidfVectorizer(),MultinomialNB())
# Trainthemodel
model.fit(X_train,y_train)
returnmodel
#Mainfunction
if_name_=="_main_":
wishMe()
intent_model=train_intent_recognition_model() # Traintheintentrecognitionmodel
whileTrue:
query=takeCommand().lower()
#Predict theintent
intent=intent_model.predict([query])[0]
ifintent=="weather":
speak("Iamunabletochecktheweather rightnow.")
elifintent=="joke":
speak("Whydon'tscientiststrustatoms?Because theymakeupeverything!")
elifintent=="timer":
speak("Settingatimerfor10minutes.")
#Codetosetatimercanbeaddedhere
elifintent=="music":
speak("Playingsomemusic.")
#Codetoplay musiccanbeaddedhere
elifintent=="time":
strTime=datetime.datetime.now().strftime("%H:%M:%S")
speak(f"DearFriend,thetimeis{strTime}")
elifintent=="recipe":
speak("Youcanmakepancakesbymixingflour,milk,andeggs.")
elifintent=="story":
speak("Onceuponatimeinafaraway land...")
elifintent=="news":
speak("Herearethelatestnewsheadlines.")
#Codetofetchnewscanbeaddedhere
elifintent=="open_youtube":
webbrowser.open("https://www.youtube.com")
elifintent=="open_google":
webbrowser.open("https://www.google.com")
elifintent=="send_email":
try:
speak("WhatshouldI mail?")
content = takeCommand()
to = "pranay@example.com" # Enter recipient's email address
sendEmail(to, content)
speak("Email has been sent to Pranay!")
except Exception as e:
print(e)
speak("Sorry my friend, I am not able to send this email.")
else:
speak("I'm sorry, I didn't understand that command.")
