import sys

# multiple of 3, 5
# Is the number one of the 3 remaining multiples of 7? 7*7, 7*11, 7*13


def is_prime(n):
    if n < 2:
        print("This is less than or equal to 1, Not prime or composite")
        return False
    elif n == 2:
        print("The number {} is prime!".format(n))
        return True
    elif n > 2 and n % 2 == 0:
        print("The number {} is even, so not prime.".format(n))
        return False
    elif n > 5 and n % 5 == 0:
        print("This number {} is not 5 but is a multiple of 5, so not prime.".format(n))
        return False
    elif n > 3 and n % 3 == 0:
        print("This number {} is not 3 but is a multiple of 3, so not prime.".format(n))
        return False
    elif n == 49 or n == 77 or n == 7 * 13:
        print("This number {} is not prime.".format(n))
        return False
    else:
        print("{} is prime!".format(n))
        return True


def get_prime(m):
    n = 0
    number_of_prime = []
    while len(number_of_prime) < m:
        n += 1
        get_num = is_prime(n)
        if get_num:
            number_of_prime.append(n)
    return number_of_prime


prime_numbers = get_prime(10001)


for numbers in prime_numbers:
    print(numbers)
