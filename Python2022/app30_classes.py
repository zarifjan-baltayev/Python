#  Class name starts with uppercase letter.
#  If class name is longer than one word (multiple word),
#  than we write words together and
#  each word starts with uppercase letter.

class Point:
   def move(self):
       print("move")

   def draw(self):
       print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
point2.y = 2
print(point2.y)

