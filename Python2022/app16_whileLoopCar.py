# print('To start the program, please right down "help"')
# user_input = str(input(">").lower())
#
# if user_input == "help":
#      print("start - to start the car")
#      print("stop - to stop the car")
#      print("quit - to exit")
#      choise = ""
#      while choise != "quit" :
#          choise = str(input(">"))
#          if choise == "start":
#                 print("The car started ... Ready to go!")
#          elif choise == "stop":
#                 print("The car stopped!")
#          elif choise == "quit":
#                 print("Bye Bye !")
#          else:
#              print("I don't understand that...")
# else:
#     print("Restart program and write down 'help' !" )



command = ""
while command != "quit":   # [command != "quit"] ----- instead of that command we can use [ True ]
    command = str(input("> ").lower())
    if command == "start":
        print("The car started...")
    elif command == "stop":
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

