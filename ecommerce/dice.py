import random
numbers = [2,3,4,5,6,1]
dice = random.choice(numbers)
print(dice)


class Dic:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice = Dic()
print(dice.roll())