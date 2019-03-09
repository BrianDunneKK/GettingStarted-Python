# How many times will you have to roll N dice before you get all sixes?
    
from random import randint

def roll_dice():
    return randint(1,6)

def roll_N_dice(n):
    dice = []
    for i in range(n):
        dice.append(roll_dice())
    return dice

def check_for_sixes(N_dice):
    return (sum(N_dice) == len(N_dice)*6)

n = int(input("How many dice will I use? "))

count = 1
while (check_for_sixes(roll_N_dice(n)) == False):
    count += 1

print("It took " + str(count) + " turns.")

dice = roll_N_dice(n)
