from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)


def roll_dice(roll_number, sides = 6):
    print(f'\nDice of {sides}-sides, be rolled {roll_number} times')

    dice = Dice(sides)

    for i in range(0, roll_number):
        print(dice.roll_dice())

roll_dice(10)
roll_dice(10, 10)
roll_dice(10, 20)
