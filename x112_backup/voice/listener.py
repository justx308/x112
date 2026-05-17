import os
import json

def listen():

    print("🎤 Listening...")

    os.system("termux-speech-to-text > voice.json")

    try:

        with open("voice.json", "r") as f:

            content = f.read().strip()

            if not content:
                print("No speech detected")
                return ""

            data = json.loads(content)

            text = data.get("text", "")

            print("You said:", text)

            return text.lower()

    except Exception as e:

        print("Voice Error:", e)

        return ""
