# for x in range(4):
#     for y in range(4):
#         print(f"({x}, {y})")
numbers = [2, 2, 2, 2, 10]

# for x_count in numbers:
#     print("x" * x_count)

# for x in numbers:
#     output = ""
#     for y in range(x):
#         output += "x"
#     print(output)

numbers = [3, 6, 2, 8, 10, 4]
max_number = 0
for top in numbers:
    if top > max_number:
        max_number = top
print(max_number)
