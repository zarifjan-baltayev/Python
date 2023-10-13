from pathlib import Path

# Absolute path
# ex: c:\Windows\users\kind\Documents\
#     /user/local/Documents
# Relative path

path = Path("ecommerce")
# print(path.mkdir())
# print(path.rmdir())

# print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)


