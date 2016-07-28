"""
calculator exercise with main() function.
main() function makes this module reusable.
"""


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def modulo(num1, num2):
    return num1 % num2


def power(base, exponent):
    return base ** exponent


def square(num1):
    return num1 ** 2


def main():
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


if __name__ == "__main__":
    print "Show the __name__ of this calculator_main.py module.", __name__
    main()
