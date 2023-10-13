import random


class Dice:

    @staticmethod
    def rolled():

        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y


dice = Dice()

print(dice.rolled())

