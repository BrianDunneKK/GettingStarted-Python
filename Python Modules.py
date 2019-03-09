# Standard import: Definitions are in module's symbol table
import Fibonacci

print (Fibonacci.__name__)

Fibonacci.fib_print(50)

fib = Fibonacci.fib_list(50)
print("01: ", fib)

fl = Fibonacci.fib_list
print ("02: ", fl(50))


# Import module definitions into global symbol table
from Fibonacci import fib_print, fib_list
print ("03: ", fib_list(50))


# Rename on import
from Fibonacci import fib_list as my_fib_list
print ("04: ", my_fib_list(50))
# Alternative: import Fibonacci as fib

print()
print("Module names:")
print(dir(Fibonacci))
print()
print("All names:")
print(dir())

# Next: https://docs.python.org/3.6/tutorial/modules.html#packages
