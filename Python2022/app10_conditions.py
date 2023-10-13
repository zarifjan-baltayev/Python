# if it is hot
#     It is a hot day
#     Drink plenty of water
# otherwise if it is cold
#     It is a cold day
#     Wear warm clothes
# otherwise
#     It is a lovely day

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It is hot to day!")
#     print("Than drink more water!")
# elif is_cold:
#     print("It is a cold day!")
#     print("Wear warm clothes...")
# else:
#     print("It is lovely day!")
#     print("Enjoy it!  :) ")

price = 1000000
is_goodCredit = False

print("Price of a house is $1000000 .")
if is_goodCredit:
    down_payment = price*0.1
else:
    down_payment = price*0.2
print(f"You must put down ${down_payment} .")