#  Dictionaries have two parts - KEY and VALUE and using {}
customer ={
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer["age"])
print(customer["is_verified"])
customer["birthday"] = "january 31 1901"
print(customer["birthday"])