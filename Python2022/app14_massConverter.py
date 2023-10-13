weight = float(input("Enter your weight : "))
mass_unit = str(input("Enter mass unit : "))

if mass_unit.upper() == "L":
    print(" Your weight is " + str(weight * 0.45) + " KG")
elif mass_unit.upper() == "K":
    print(" Your weight is " + str(weight / 0.45) + "LBS")  # / float, // integer
else:
    print("Your entered values are wrong!")
