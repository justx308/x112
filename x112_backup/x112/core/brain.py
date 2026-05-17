from automation.actions import run_action
from memory.memory import save_memory, load_memory, show_memory

def think(command):

    command = command.lower()

    # MEMORY SAVE
    if command.startswith("remember"):

        data = command.replace("remember", "").strip()

        if " is " in data:

            key, value = data.split(" is ", 1)

            save_memory(key.strip(), value.strip())

            print(f"🧠 Remembered: {key} = {value}")

        else:
            print("Format: remember name is Jasco")

    # MEMORY RECALL
    elif command.startswith("what is"):

        key = command.replace("what is", "").strip()

        value = load_memory(key)

        print(f"🧠 {key} = {value}")

    # SHOW ALL MEMORY
    elif command == "show memory":

        memories = show_memory()

        print("🧠 MEMORY DATABASE:")
        print(memories)

    # ACTIONS
    elif "torch on" in command:
        run_action("torch_on")

    elif "torch off" in command:
        run_action("torch_off")

    elif "battery" in command:
        run_action("battery")

    elif "open mt5" in command:
        run_action("mt5")

    elif "time" in command:
        run_action("time")

    else:
        print("Unknown command")
