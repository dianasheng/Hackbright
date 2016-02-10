def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

input_number = int(raw_input("Enter a number to check if it's prime. "))

if is_prime(input_number):
    print "%i is a prime number." % (input_number)
else: print "%i is not a prime number." % (input_number)
