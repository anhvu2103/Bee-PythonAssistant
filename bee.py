import speech_recognition
import pyttsx3
from gtts import gTTS
import webbrowser
import smtplib

#START
#Listen
bee_brain = ""
bee_ear = speech_recognition.Recognizer()
#initialize
bee_speaking = pyttsx3.init()
print("It's on")

def myBee():
	while True:
		with speech_recognition.Microphone() as mic:
			audio = bee_ear.listen(mic)
		try:
			you = bee_ear.recognize_google(audio)
		except:
			you = "...."
		print(you)

		#Reply in words
		if you == "hello":
		    bee_brain = "Hello! How may I help you?"

		elif you == "what is your name":
			bee_brain = "My name is Bee"

		elif you == "do you know me":
			bee_brain = "Yes! You are my brother"

		elif you == "do you know my name":
			bee_brain = "Yes! Your name is Anh"

		elif you == "how are you":
			bee_brain = "chillin"

		elif you == "open Instagram":
			bee_brain = "I'm on it..."
			webbrowser.open('http://www.instagram.com')

		elif you == "open YouTube":
			bee_brain = "You got it.."
			webbrowser.open('http://www.youtube.com')
		else 
			break;


		print("Bee:", bee_brain)

		#reply with voice
		#test
		bee_speaking.say(bee_brain)
		bee_speaking.runAndWait()

myBee()