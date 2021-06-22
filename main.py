import speech_recognition as sr
import os
import auto_click

def getParams(phrase):
    auto_click.defIdentify(phrase)

def startRecognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo: ")
        audio = r.listen(source)
        texto = r.recognize_google(audio, language='pt-BR')

        try:
            getParams(texto)
        except Exception as err:
            print(err)

startRecognize()