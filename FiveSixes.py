# How many times will you have to roll 5 dice before you get 5 sixes?

from random import randint

def roll_dice():
    return randint(1,6)

def roll_five_dice():
    return ([roll_dice(), roll_dice(), roll_dice(), roll_dice(), roll_dice()])

def check_for_sixes(five_dice):
    return (sum(five_dice) == 30)
    
count = 1
while (check_for_sixes(roll_five_dice()) == False):
    count += 1

print("It took " + str(count) + " turns.")
