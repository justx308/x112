import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_action(action):

    if action == "torch_on":
        os.system("termux-torch on")
        speak("Torch activated")

    elif action == "torch_off":
        os.system("termux-torch off")
        speak("Torch disabled")

    elif action == "battery":
        os.system("termux-battery-status")

    elif action == "mt5":
        os.system("am start -n net.metaquotes.metatrader5/.ui.MainActivity")
        speak("Opening MetaTrader 5")

    elif action == "time":
        os.system("date")
