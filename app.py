from core.brain import think
import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

print("================================")
print("        X112 AI ONLINE         ")
print("================================")

speak("X112 online")

while True:

    command = input("X112 >>> ")

    if command.lower() == "exit":
        speak("Shutting down")
        break

    think(command)
