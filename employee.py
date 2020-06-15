class Employee:
    def __init__(self):
        self.__name = " "
        self.__designation = " "
        self.__salary = 0

    def set_name(self, name):
        self.__name = name

    def set_designation(self, designation):
        self.__designation = designation

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_designation(self):
        return self.__designation

    def get_salary(self):
        return self.__salary

    def calculate_bonus(self):
        if Employee.get_designation(self) == 1:
            return 0.10 * Employee.get_salary(self)
        elif Employee.get_designation(self) == 2:
            return 0.15 * Employee.get_salary(self)
        elif Employee.get_designation(self) == 3:
            return 0.20 * Employee.get_salary(self)

    def total_salary(self):
        return Employee.calculate_bonus(self) + Employee.get_salary(self)

    def __str__(self):
        return "Name: {}\nBonus: {}\nTotal Salary: {}\n" \
               .format(Employee.get_name(self),
                       round(Employee.calculate_bonus(self), 2),
                       round(Employee.total_salary(self), 2))


