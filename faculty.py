import random


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__emp_id = 0
        self.__salary = salary

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_emp_id(self):
        self.__emp_id = random.randint(1, 65300)

    def set_salary(self, salary):
        self.__salary = salary

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary

    def get_full_name(self):
        return self.get_first_name() + " " + self.get_last_name()


class Faculty(Employee):
    def __init__(self, first_name, last_name, salary):
        Employee.__init__(self, first_name, last_name, salary)
        self.__department = " "
        self.__specialization = " "

    def set_department(self, department):
        self.__department = department

    def set_specialization(self, special):
        self.__specialization = special

    def get_department(self):
        return self.__department

    def get_specialization(self):
        return self.__specialization

    def __str__(self):
        return "Name: {}\nID: {}\nSalary: ${}\nDepartment: {}\nSpecialization: {}\n"\
            .format(self.get_full_name(), self.get_emp_id(), self.get_salary(),
                    self.get_department(), self.get_specialization() )