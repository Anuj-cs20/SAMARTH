import speech_recognition as sr

# create an instance of the recognizer
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    # listen for the audio and store it in a variable
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))
