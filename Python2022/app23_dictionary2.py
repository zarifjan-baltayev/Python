# phone: 1234
# One Two Three Four

numbers = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"
}

phone_number = str(input("Please enter your phone number : "))
output = ""
for x in phone_number:
    y = int(x)
    output += numbers.get(y, "!") + "  "
print(output)