import speech_recognition 
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio_data)
            text = text.lower()

            printf(f"Recognized {text}")
    except speech_recognition.UnknwonValueError():

        recognizer = speech_recognition.Recognizer()
        continue