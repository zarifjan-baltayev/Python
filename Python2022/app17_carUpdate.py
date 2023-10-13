command = ""
started = False
while command != "quit":   # [command != "quit"] ----- instead of that command we can use [ True ]
    command = str(input("> ").lower())
    if command == "start":
        if started:
            print("The car already started!")
        else:
            started = True
            print("The car started...")
    elif command == "stop":
        if not started:
            print("The car already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        spot  - to stop the car..
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print(" I don't understand that...")