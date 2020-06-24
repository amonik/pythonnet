class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_full_name(self):
        return self.get_first_name() + " " + self.get_last_name()


class Student(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)
        self.__degree = " "
        self.__gpa = 0

    def set_degree(self, degree):
        self.__degree = degree

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_degree(self):
        return self.__degree

    def get_gpa(self):
        return self.__gpa

    def __str__(self):
        return "Name: {}\nDegree: {}\nGPA: {}\n".format(self.get_full_name(), self.get_degree(), self.get_gpa())
