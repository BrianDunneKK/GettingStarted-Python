from random import randint

def roll_dice():
    return randint(1,6)

for i in range(3):
    dice = roll_dice()
    print(dice)
