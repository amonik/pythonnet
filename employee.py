class Employee:
    """ Intialize the varibles"""
    def __init__(self):
        self.__name = " "
        self.__designation = " "
        self.__salary = 0

    """All the getters and setters are used because we use private variables with __"""
    """The set_name method sets the set_name attribute"""
    def set_name(self, name):
        self.__name = name

    """The set_designation method sets the set_designation attribute"""
    def set_designation(self, designation):
        self.__designation = designation

    """The set_salary method sets the set_salary attribute"""
    def set_salary(self, salary):
        self.__salary = salary

    """"The get_name method it the returns the name attribute"""
    def get_name(self):
        return self.__name

    """The get_designation method it returns the designation attribute"""
    def get_designation(self):
        return self.__designation

    """The get_salary method it returns the salary attribute"""
    def get_salary(self):
        return self.__salary

    """Calculate the bonus based on input from the user, calls get_designation method"""
    def calculate_bonus(self):
        if Employee.get_designation(self) == 1:
            return 0.10 * Employee.get_salary(self)
        elif Employee.get_designation(self) == 2:
            return 0.15 * Employee.get_salary(self)
        elif Employee.get_designation(self) == 3:
            return 0.20 * Employee.get_salary(self)

    """Calculates the total salary by calling the calculate_bonus and get_salary methods and adding them"""
    def total_salary(self):
        return Employee.calculate_bonus(self) + Employee.get_salary(self)

    """Used for printing the current state of the variables, it also calls various methods above"""
    def __str__(self):
        return "Name: {}\nBonus: {}\nTotal Salary: {}\n" \
               .format(Employee.get_name(self),
                       round(Employee.calculate_bonus(self), 2),
                       round(Employee.total_salary(self), 2))


