## Source: https://docs.python.org/3.6/index.html

## Numeric data types ##
# int, float, complex
# Additional numeric types: decimal, Fraction
#
#  **  Exponential
#  //  Floor division
#  %   Modulo

## Strings ##
# Single or double quotes
# Prefix with r for raw string (e.g. print(r'C:\some\name'))
# Immunatable
# Use triple quotes for muliple line strings
#
#  +      Concatenation (optional for sting constants)
#  *      Repeat string
#  []     String index (0 is first char, -1 is last char)
#  [a:b]  Slice index; from position a (inc) to b (exc); omit a/b for start/end
#  len(s) Length

## List class ##
#  sq = [1,4,9,16,25,36]
#  [i]    Index (returns item)
#  [a:b]  Slice (returns new list)
#  +      Concatenate
#  sq[:]  Shallow copy
#  sq[2] = 88    Change item 3
#  sq[2:5] = []  Remove items 3, 4 & 5
#  sq[:] = []    Clear list
#  len(sq)       Length
n = [['a', 'b', 'c'], [1, 2, 3]]  # Nested lists
print ("n[0][2] =", n[0][2])      # Returns 'c'


## Range ##
# Iterable, not a list
r5=range(5)   # (stop); 0,1,2,3,4
range(2,15,3) # (start, stop[, step]); 2,5,8,11,14
print(list(r5))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

## Misc
#  _  Last result

## Control flow ##
# if
#x = int(input("Please enter an integer: "))
x = -23
if x < 0:
    print(x, 'is negative')
elif x == 0:
    print('Zero')
else:
    print(x, 'is positive')

# while
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b      # Fibonacci series
print()

# for
words = ['cat', 'window', 'defensive']
for w in words:
    print(w, len(w))

# break, else, continue
print ("Primes:", end=" ")
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            # Not a prime
            break # Stop ierating ("for x") and skip the "else:" block
    else: # Run when "for x" loop completes
        print(n, end=',')
# continue jumps to the end of the loop, followed by the next iteration
print()

# pass
# Does nothing (no-op)

## Functions ##
def fib(n):    # Arguments are call by object reference (value)
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # Same as "result = result + [a]" but more efficient
        a, b = b, a+b
    return result  # If there is not return, None is returned

print("Fibonacci:", fib(1000), end=" ")
print("\n", fib.__doc__)
print()

# Default Arguments, "in" operator, User input, Raise exception, Keyword args
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#ask_ok('Do you really want to quit?')
#ask_ok('OK to overwrite the file?', 2)
#ask_ok("Are you sure?", reminder="Have another go!")

# Mutable arguments persist between function calls
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# Variadic arguments: *name and **name
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    print("-" * 40)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very,", "VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Unpacking a list/tuple/dictionaries
k = "Limburger"
l = ["It's very runny, sir.", "It's really very,", "VERY runny, sir."]
d = {"shopkeeper": "Michael Palin", "client": "John Cleese",
     "sketch": "Cheese Shop Sketch"}
cheeseshop(k, *l, **d)

# Annotations
def ham_eggs(ham: str, eggs: str = 'eggs') -> int:
    return len(ham) + len(eggs)

print("Should be 7: ", ham_eggs("abc", "defg"))
print("Annotations: ", ham_eggs.__annotations__)
