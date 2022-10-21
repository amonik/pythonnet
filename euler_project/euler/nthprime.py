import sys

# multiple of 3, 5
# Is the number one of the 3 remaining multiples of 7? 7*7, 7*11, 7*13


def is_prime(n):
    if n < 2:
        print("This is less than or equal to 1, Not prime or composite")
        sys.exit()
    elif n == 2:
        print("The number {} is prime!".format(n))
    elif n > 2 and n % 2 == 0:
        print("The number {} is even, so not prime.".format(n))
        sys.exit()
    elif n > 5 and n % 5 == 0:
        print("This number {} is not 5 but is a multiple of 5, so not prime.".format(n))
    elif n > 3 and n % 3 == 0:
        print("This number {} is not 3 but is a multiple of 3, so not prime.".format(n))
    elif n > 7 and n % 7 == 0:
        print("This number {} is not 7 but is a multiple of 7, so not prime.".format(n))
    else:
        print("{} is prime!".format(n))


is_prime(564897)
