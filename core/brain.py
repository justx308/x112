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
            print("Format: remember name is x112")

    # MEMORY RECALL
    elif command.startswith("what is"):

        key = command.replace("what is", "").strip()

        value = load_memory(key)

        print(f"🧠 {key} = {value}")

    # SHOW MEMORY
    elif command == "show memory":

        print(show_memory())

    # BASIC COMMANDS
    elif command == "battery":
        import os
        os.system("termux-battery-status")

    elif command == "open mt5":
        import os
        os.system("am start -n net.metaquotes.metatrader5/.ui.MainActivity")
        print("🚀 Opening MT5")

    elif command == "time":
        import os
        os.system("date")

    else:
        print("Unknown command")	
