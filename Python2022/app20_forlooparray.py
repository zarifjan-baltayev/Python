# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[2][2] = 90
# print(matrix[0][1])
# for raw in matrix:
#     for x in raw:
#         print(x)

numbers = [5, 9, 2, 5, 7, 3, 4]
numbers2 = numbers.copy()
numbers.append(10)
numbers.insert(0, 1)
numbers.sort()
numbers.reverse()
numbers.remove(1)
numbers.pop()
numbers.clear()
numbers2
print(numbers2.index(9))
print(50 in numbers2)
print(numbers2.count(5))
numbers2.sort()
print(numbers2)
equal = 0
for x in numbers2:
    if equal == x:
        numbers2.remove(x)
    else:
        equal = x
print(numbers2)

#  ANOTHER WAY of To Get Rid Of Repeated Numbers
numbers = [7, 7, 8, 8, 5, 5, 9, 2, 2]
uniques =[]

print(numbers)
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)