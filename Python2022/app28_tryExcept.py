try:
    age = int(input("Age > "))
    income = 20000
    risk = income / age
    print(f'Your risk is : {risk}')
    print("Yor age is : " + " " + str(age))
except ZeroDivisionError:
    print("Age can not be zero!")
except ValueError:
    print("Invalid value, please enter integer number?!")
