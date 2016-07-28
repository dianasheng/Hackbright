"""
Demo to show how adding a main() function makes a module reusable.
"""
from calculator import *  # uses file without main() function
#from calculator_main.py import * # uses file without main() function

print __name__

# (4+5) + (9-6)
print add(add(4, 5), subtract(9, 6))

# (12/2) - 60
print subtract(divide(12, 2), 60)

# 1 + 2 + 3
print add(add(1, 2), 3)

# (1 + 2)^2
print square(add(1, 2))

# (3%4) / 9*9
print divide(modulo(3, 4), multiply(9, 9))

# 7 * (3+8)
print multiply(7, add(3, 8))

# (1+2) - 3 * (4+5)
print subtract(add(1, 2), multiply(3, add(4, 5)))

# 3^(2+3)
print power(3, add(2, 3))

