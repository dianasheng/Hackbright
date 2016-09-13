import math


# this is the conventional way of defining a function
def square_root(x):
    return math.sqrt(x)

print square_root(9)

# use a lamba function to do the same thing
square_root1 = lambda x: math.sqrt(x)
print square_root1(9)


# conventional way of defining a function
def double(x):
    return x * 2

print double(20)

# use a lamba function to do the same thing
double1 = lambda x: x * 2
print double1(20)