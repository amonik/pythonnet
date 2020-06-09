class Salary:
    """Consturctor that initializes the variables"""
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward
    """Function that takes no variables but returns the annual_salary"""
    def annual_salary(self):
        return (self.pay * 12) + self.reward


class Employee:
    def __init__(self, name, position, pay, reward):
        self.name = name
        self.position = position
        self.total_salary = Salary(pay, reward)

    def final_salary(self):
        return self.total_salary.annual_salary()


employee = Employee("Amon", "Automation", 50000, 25000)
print(employee.final_salary())
