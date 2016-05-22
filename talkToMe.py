import sys
import pyaudio
import monotonic

# github/uberi/speech_recognition
import speech_recognition as sr

# bring in tone analyzer
import json
from watson_developer_cloud import ToneAnalyzerV3Beta


# get audio from mic
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Listening for input...")
	audio = r.listen(source)

# Watson Credentials
IBM_USERNAME = ""
IBM_PASSWORD = ""

try:
	audOut = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
	print("Watson thinks you said: " + audOut)
except sr.UnknownValueError:
	print("WHAT DID YOU SAY!? - Watson")
except sr.RequestError as e:
	print("WATSONS DOWN OR SOMETHING; {0}".format(e))


TONE_USERNAME = ""
TONE_PASSWORD = ""
TONE_VERSION = ""

tone_analysis = ToneAnalyzerV3Beta(username=TONE_USERNAME, password=TONE_PASSWORD, version=TONE_VERSION)

print(json.dumps(tone_analysis.tone(text=audOut), indent=2))
