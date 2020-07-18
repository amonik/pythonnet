# Define the main function with error correction to ask the user for the numbers.
def main():
    while True:
        try:
            m = int(input("Please enter in a number for m >= 0: "))
            break
        except ValueError:
            print("Must be a non-negative number. ")
        except RuntimeError:
            print("Must be positive")
    while True:
        try:
            n = int(input("Please enter in a second number for n >= 0: "))
            break
        except ValueError:
            print("Must be a non-negative number. ")
    # This exception catch is needed or if the person enters in negative numbers and exception is thrown.
    try:
        print(ackermann(m, n))
    except RecursionError as re:
        print('Sorry but this Ackermann solver was not able to finish.\n'
              'Please run the program again with positive numbers.\n'
              'This problem does not accept numbers less then zero\n'
              'or the recursion is too large.'
              '({})'.format(re.args[0]))


# Define mathematical function for Ackermann, which takes non-negative integers m and n.
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


if __name__ == '__main__':
    main()




