birth_year = input('Please enter your year of birth? :')
print(type(birth_year))
age = 2023 - int(birth_year)
print(type(age))
print('You are ' + str(age) + ' years old! ')

weight_lbs = input('Enter your weight in pound! :')
weight_kg = float(weight_lbs) * 0.45359237
print('Your waight is ' + str(weight_kg) + ' kilograms!')
