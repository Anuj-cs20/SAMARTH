import os
import speech_recognition as sr
import subprocess
PROMPT = ""

# set up Google Cloud Speech API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"samarth-warpspeed-8503d69efe59.json"
r = sr.Recognizer()

# set up audio source
with sr.Microphone() as source:
    print("Hi! I am SAMARTH")
    print("How can I assist you today...")
    audio = r.listen(source)

# recognize speech using Google Cloud Speech API
try:
    text = r.recognize_google_cloud(audio)
    # print(text)
    if "assistant" in text.lower():
        text = text.lower().split("assistant", 1)[-1].strip()
        PROMT = text
        print("You said: " + text)
        subprocess.Popen(f"python3.10 main.py {PROMT}", shell=True)
        # os.system('python3.10 test.py')
        # exec(open('test.py').read())
except sr.UnknownValueError:
    print("Google Cloud Speech API could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Cloud Speech API service; {0}".format(e))
