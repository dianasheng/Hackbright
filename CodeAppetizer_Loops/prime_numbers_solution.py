"""
Prime number code appetizer Part 1 and 2.
"""


def is_prime(number):
    for i in range(2, number):
        # not a prime if number is divisible by any number from 2 to itself.
        if number % i == 0:
            return False
    return True


def main():
    while True:
        input_number = int(raw_input("Enter a number to check if it's prime. "))

        if is_prime(input_number):
            print "%i is a prime number." % (input_number)
        else:
            print "%i is not a prime number." % (input_number)


if __name__ == '__main__':
    main()
