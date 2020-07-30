""""
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


class InvalidInput(ValueError):
    def __init__(self, my_input):
        super().__init__(f"You enter in incorrect value ${my_input}")
"""


from tkinter import *
from tkinter import messagebox


class WidgetDemo():
    def __init__(self):
        window = Tk()
        window.title("Widget Demo!")
        frame1 = Frame(window)
        frame1.pack()

        button1 = Button(window, text="The Button", command=self.processButton())
        button1.pack()

        window.mainloop()

    def processButton(self):
        my_message = messagebox.showinfo("Welcome")
        return my_message


WidgetDemo()
"""


class InvalidInput(ValueError):
    def __init__(self, my_input):
        super().__init__(f"You enter in incorrect value {my_input}")
        self.my_input = my_input


class Area:
    def __init__(self):
        self.x = 0

    def set_x(self, n):
        if n <= 0:
            raise InvalidInput(n)
        else:
            self.x = n

    def __str__(self):
        return str(self.x)


def main():
    a = Area()
    input_value = int(input("Enter in a value greater than 0: "))
    a.set_x(input_value)
    if input_value <= 0:
        print("Invalid input entered")
    else:
        print(a)


if __name__ == '__main__':
    main()
"""







