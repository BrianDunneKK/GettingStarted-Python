########################################
print ("#### List class ####")

# Methods:
#  append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy

## Basics
sq = [0,1,4,9,16,25,36,49,64,81]
print(sq)
print(sq[3])            # Index (returns item)
print(sq[4:6])          # Slice (returns new list)
print(len(sq))          # Length
print(sq+[100,121,144]) # Concatenate
sq[7] = 4949            # Change item 8 (or del sq[7])
sq[2:5] = []            # Remove items 3, 4 & 5 (or del sq[2:5])
print(sq)
sq[:] = []              # Clear list (or del sq[:])
print(sq)
#  sq[:]  Shallow copy

n = [['a', 'b', 'c'], [1, 2, 3]]  # Nested lists
print ("n[0][2] =", n[0][2])      # Returns 'c'
print()

## List comprehensions
# List of squares
squares = [0,1,4,9,16,25,36,49,64,81]
print(squares)

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

for i, sq in enumerate(squares):  # i = Position index
    print(i, sq)

print()

# Dice combinations
dice_all = [(x, y) for x in list(range(1,7)) for y in list(range(1,7))]
print(dice_all)

# Dice combinations excluding doubles
dice_ex2 = [(x, y) for x in list(range(1,7)) for y in list(range(1,7)) if x != y]
print(dice_ex2)

dice_ex2 = [(x, y) for (x,y) in dice_all if x != y]
print(dice_ex2)

# Dice totals
dice_total = [(x, y, x+y) for (x,y) in dice_all]
print(dice_total)

# Flatten list
dice_flat = [die for dice in dice_all for die in dice]
print(dice_flat)
print()

# Nested list comprehensions
# See https://docs.python.org/3.6/tutorial/datastructures.html#nested-list-comprehensions

########################################
print ("### Tuples ###")

# Immutable, heterogeneous sequence of elements

tup1 = (12345, 54321, 'hello!')  # Tuple packing
tup2 = tup1, (1, 2, 3, 4, 5)
print (tup1)
print (tup2)

tup_empty = ()
tup_singleton = 'hello',  # Trailing comma
print (tup_empty)
print (tup_singleton)

x, y, s = tup1  # Sequence unpacking
print("x:", x, ", y:", y, "s:", s)

# Tuples iterator
questions = ['colour', 'food', 'sport']
answers = ['blue', 'meatballs', 'hurling']
for q, a in zip(questions, answers):
    print('Favourite {0}: {1}'.format(q, a))

print()

########################################
print ("### Sets ###")

# Unordered collection with no duplicate elements

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} # Duplicates are removed
print(basket)

print ('orange' in basket)  # True
print ('lemon' in basket)   # False

a = set('abracadabra')
b = set('alacazam')

print ("a:", a)
print ("b:", b)
print ("a-b:", a - b)   # Difference (in a, not in b)
print ("a|b:", a | b)   # Union
print ("a&b:", a & b)   # Intersection
print ("a^b:", a ^ b)   # Symmetric difference (in a or b but not both)
print ("(a|b) - ((a^b) | (a&b)):", (a|b) - ((a^b) | (a&b)))  # Empty set

# Set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print (a)
print()


########################################
print ("### Dictionaries ###")
# Unordered set of key-value pairs; keys are unique
# Indexed by keys, which can be any immutable type (strings, numbers, tuples)

emp = {'Jack': 4098, 'Jane': 4139}
emp['John'] = 4127
print(emp)
print ("Jane:", emp['Jane'])
del emp['Jack']
emp['Judy'] = 4127
print (emp)
print ("Keys:", list(emp.keys()))
print ("Keys (Z-A):", sorted(emp.keys(), reverse=True))
print ("?Judy:", 'Judy' in emp)
print ("?Jack:", 'Jack' in emp)
       
# dict() constructor
emp = dict([('Jack', 4139), ('Jane', 4127), ('John', 4098)])
print(emp)

emp = dict(Jack=4098, Jane=4139, John=4127)
print(emp)

name = ['Jack', 'Jane', 'John']
code = [4139, 4127, 2098]
emp = dict(zip(name, code))
print(emp)

# Iterating
for k, v in emp.items():
    print(k, " = ", v)
 

# dict comprehension
d = {x: x**2 for x in (2, 4, 6)}
print (d)

# Next: https://docs.python.org/3.6/tutorial/datastructures.html#looping-techniques
