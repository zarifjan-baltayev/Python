

# ==  !=  >  >=  <  <=

# if name is less than 3 characters long
#     name must be at least 3 characters
# if name is more than 50 characters long
#     name can be maximum 50 characters
# otherwise
#     name looks good

name = "John Smith"

if len(name) < 3:
    print("Name must be at least 3 characters!")
elif len(name) > 50:
    print("Name can be maximum 50 characters!")
else:
    print("The name looks good!")





