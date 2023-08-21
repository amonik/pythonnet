import math
import sys


def get_factorial(num):
    total = 0
    for i in str(num):
        total += math.factorial(int(i))
    if num == total:
        return True
    else:
        return False


def main():
    my_sum_factorial = 0
    for num in range(3, 999999):
        if get_factorial(num):
            my_sum_factorial += num
    return my_sum_factorial


if __name__ == '__main__':
    print(main())
