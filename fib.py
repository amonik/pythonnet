def main():
    print(cal(8))


def cal(n):

    if n > 0:
        n += cal(n - 1)
    return n


if __name__ == '__main__':
    main()


class Person:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

       
class Patient(Person):
    def __init__(self, name, sickness):
        self.__sickness = sickness
        Person.__init__(name)

    def set_sickness(self, sickness):
        self.__sickness = sickness

    def get_sickness(self):
        return self.__sickness





