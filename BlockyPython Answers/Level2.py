question = 101

if question == 1:
    age = input("What age are you? ")
    next_age = int(age) + 1
    print("At your next birthday, you will be " +
          str(next_age) + " years old.")

if question == 2:
    age = input("What age are you? ")
    twice_age = int(age) * 2
    print("If you were twice as old, you’d be " + str(twice_age))

if question == 3:
    word = input('Enter a word: ')
    msg = 'The word {} has {} letters.'.format(word, len(word))
    print(msg)

if question == 4:
    word = input('Enter a 4-letter word: ')
    if len(word) == 4:
        print('Correct! That is a 4-letter word.')
    else:
        print('Wrong! That is not a 4-letter word.')


if question == 5:
    first_num = int(input('Enter a number: '))
    second_num = int(input('Enter a different number: '))
    if first_num != second_num:
        print('Correct! They are different numbers.')
    else:
        print('Wrong! They are the same numbers.')

if question == 6:
    num = int(input('Enter a small number: '))
    if num <= 10:
        print('That number is a good choice!')
    elif num < 100:
        print('That number is too big.')
    else:
        print('That number is way too big.')

if question == 7:
    num = int(input('Enter a number: '))
    for i in range(0, 11):
        msg = '{} x {} = {}'.format(num, i, num*i)
        print(msg)

if question == 8:
    num = int(input('Enter a number: '))
    if num % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")


import random

def random10():
    return random.randint(1, 10)

if question == 91:
    for i in range(3):
        print(random10())

if question == 92:
    total_random = 0
    for i in range(3):
        random_num = random10()
        total_random = total_random + random_num
        print(random_num)
    print("Total = " + str(total_random))

if question == 93:
    count_random = int(input('How many random numbers? '))
    total_random = 0
    for i in range(count_random):
        random_num = random10()
        total_random = total_random + random_num
        print(random_num)
    print("Total = " + str(total_random))


if question == 101:
    i = 1
    while (i<=50):
        if (i%3 == 0):
            print ("Fizz")
        elif (i%5 == 0):
            print ("Buzz")
        else:
            print (str(i))
        i = i + 1

if question == 102:
    i = 1
    while (i<=50):
        if (i%3 == 0 and i%5==0):
            print("Pop")
        elif (i%3 == 0):
            print ("Fizz")
        elif (i%5 == 0):
            print ("Buzz")
        else:
            print (str(i))
        i = i + 1
