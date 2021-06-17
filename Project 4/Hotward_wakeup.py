import os
import speech_recognition as sr

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print('Recognizing...')  
        query = r.recognize_google(audio)  
        query = query.lower()
        query = query.replace('jarvis','')
        print(f"User Said:{query}")

    except:
        
        return "none"
    return query    
  
while True:
    wake_up = takecommand().lower()
    
    if 'wake up' in wake_up:
        os.startfile('D:\\Language courses\\Pyhton\\Project 4\\jarvis.py')

    else:
        print('Nothing....')    
