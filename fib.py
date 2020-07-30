def main():
    print(cal(8))


def cal(n):

    if n > 0:
        n += cal(n - 1)
    return n


if __name__ == '__main__':
    main()

