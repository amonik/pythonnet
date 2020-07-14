import random


class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_name(self):
        return self.get_first_name() + " " + self.get_last_name()


class Customer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.__customer_id = ""
        self.__customer_email = ""

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_customer_email(self):
        return self.__customer_email

    def set_customer_email(self, email):
        self.__customer_email = email

    def get_customer_info(self):
        return self.get_name() + ", " + self.get_customer_email()


class Employee(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.emp_id = ""
        self.emp_salary = 0.0

    def set_emp_id(self):
        self.emp_id = random.randint(0, 12342)

    def get_emp_id(self):
        return self.emp_id

    # Add exception here
    def set_emp_salary(self, s):
        self.emp_salary = s
        if self.emp_salary < 20000:
            raise Exception("{} you need at least $20,000 to get a"
                            " bonus".format(Employee.get_name(self)))

    def get_emp_salary(self):
        return self.emp_salary

    def calculate_bonus(self):
        return self.emp_salary * 0.20
    """
    def __str__(self):
        print("The current Employee details on bonus:\nEmployee ID: {}\nEmployee name: {}\nSalary: "
              "{}\nBonus: {}\nTotal Salary: {}".format(self.get_emp_id(), Employee.get_name(self),
                                                       self.get_emp_salary(), self.calculate_bonus(),
                                                       self.get_emp_salary() + self.calculate_bonus()))
    """
    # Class inheriting ValueError class
    class NotTwentyK(ValueError):
        def __init__(self, args):
            super().__init__(args)
