import pyttsx3
import speech_recognition as sr

#pyttsx3 used , text to speech function
def speak(text): 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #print(voices)
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',Id)
    #for voice in voices:
    #   print(voice.id)    
    #   print(voice.name)
    engine.say(text=text)
    engine.runAndWait()
#speak('hello world')

#speech_recognition is used 

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 0) as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio =  r.listen(source,0,8)

    try:
        print('Recognizing.....')
        query = r.recognize_google(audio,language="en")
        return query.lower()
        
    except:
        return ""


speechrecognition()

