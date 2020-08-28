import os
import pyttsx3

print()
print("====================================================================")
print("------------------Welcome to my Automation Program------------------")
print("====================================================================")
pyttsx3.speak("Welcome Sami , Starting Your Program")
print()
pyttsx3.speak("Hello Sami ! How are you doing today ")
x = input("Hello Sami ! How are you doing today!: ")


if ("good" in x) or ("Good" in x) or ("great" in x) and ("Great" in x):
    pyttsx3.speak("Thats Nice")
    print("Thats Nice")
elif ("bad" in x) or ("not much" in x):
    pyttsx3.speak("Sorry to hear about that")
    print("Sorry to hear about that")

pyttsx3.speak("Do you want me to do something for you:")
y = input("Do you want me to do something for you: ")

if ("chrome" in y) or ("browser" in y) or ("internet" in y) or ("browse" in y):
    pyttsx3.speak("Starting Chrome")
    os.system("start chrome")
elif ("spotify" in y) or ("music" in y) or ("song" in y):
    pyttsx3.speak("Play some good songs sir")
    os.system("start spotify")
elif ("firefox" in y) or ("fox" in y):
    pyttsx3.speak("Opening Firefox")
    os.system("start firefox")
elif ("notepad" in y) or ("editor" in y):
    pyttsx3.speak("Opening NotePad")
    os.system("start notepad")
else:
    print("Bye")
