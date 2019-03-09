import msvcrt
import random
import time


def generate(left, right, pos, total):
    if (left + right) > (total - 2):
        left = int(total/2) - 1
        right = int(total/2) - 1
    left_str = ">" * left
    right_str = "<" * right
    pos_str = "X"
    space_left = " " * (pos - left)
    space_right = " " * (total - pos - right)
    return left_str + space_left + pos_str + space_right + right_str

quit_now = False
left = 15
right = 15
pos = 40
total = 80
print(generate(left, right, pos, total))

while not quit_now:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        s = str(key)
        if str(key) == "b'q'":
            pos = pos - 1
        elif str(key) == "b'w'":
            pos = pos + 1
        elif str(key) == "b'x'":
            quit_now = True
    else:
        rnd = random.randint(1, 5) - 3
        left = left + rnd
        left = max (left, 1)
        left = min (left, total - 5)
        rnd = random.randint(1, 5) - 3
        right = right + rnd
        right = max (left, 1)
        right = min (left, total - 5)
    print(generate(left, right, pos, total))
    time.sleep(0.1)
