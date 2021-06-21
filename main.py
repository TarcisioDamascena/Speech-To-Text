import speech_recognition as sr
import os
import autoClick

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga algo: ")
    audio = r.listen(source)

    texto = r.recognize_google(audio, language='pt-BR')

    try:
        print("Você disse: " + texto)
    except:
        print("Não entendi nada!")