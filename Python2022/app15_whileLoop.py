
i = 1
while i <= 6:
    print('*  ' * i)
    i += 1
    
print("Well Done!")



secret_number = 9
gess_limit = 3
gess_counter = 0

while gess_counter < gess_limit:
    gess_number = int(input("Gess the secret number! :"))
    if gess_number == secret_number:
        print("You are right! Well Done!!")
        break
    gess_counter += 1
else:
    print("You lose the game. Sorry!")
