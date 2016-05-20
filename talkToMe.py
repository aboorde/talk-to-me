import sys
import pyaudio
import monotonic

# github/uberi/speech_recognition
import speech_recognition as sr

# get audio from mic
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Listening for input...")
	audio = r.listen(source)

# Watson Credentials
IBM_USERNAME = ""
IBM_PASSWORD = ""

try:
	print("Watson thinks you said: " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
	print("WHAT DID YOU SAY!? - Watson")
except sr.RequestError as e:
	print("WATSONS DOWN OR SOMETHING; {0}".format(e))
