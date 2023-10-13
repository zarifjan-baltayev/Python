class Mommal:
    def walk(self):
        print(f"The animal is walking.")


class Dog(Mommal):
    def bark(self):
        print("Barking")


class Cat(Mommal):
    def annoying(self):
        print("The cat annoying!")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 =Cat()
cat1.walk()
cat1.annoying()

