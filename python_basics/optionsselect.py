import os
import pyttsx3

pyttsx3.speak("Welcome to Select Option Program")

print()
print("------------Welcome to Select Option Program------------\n")
print("Enter 1: To open Chrome")
print("Enter 2: To open Notepad")
print("Enter 3: To open Firefox")
print()
x=int(input("Enter Your Choice\n"))

if x == 1 :
	pyttsx3.speak("opening chrome ! Stay Calm")
	os.system("start chrome")
elif x==2 :
	pyttsx3.speak("opening notepad")
	os.system("start notepad")
elif x==3 :
	pyttsx3.speak("opening firefox | Get Ready")
	os.system("start firefox")
else:
	pyttsx3.speak("Ohooooooo You are Lost")
	print("Error | You are Lost ")

