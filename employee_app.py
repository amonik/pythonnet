from customer import Employee

# Employee with at least 20,000 and not exception is raised.
emp_good = Employee('Stephanie', 'Tian')
emp_good.set_emp_id()
emp_good.set_emp_salary(35000)
bonus = emp_good.calculate_bonus()
print("The current Employee details on bonus :")
print(emp_good.get_name())
print("Employee ID : ", emp_good.get_emp_id())
print("Salary :", emp_good.get_emp_salary())
print("Bonus :", bonus)
print("Total Salary :", bonus + emp_good.get_emp_salary())


# Exception will be raised, because he salary is less than 20,000.
emp_low = Employee('Doug', 'Donald')
emp_low.get_name()
emp_low.set_emp_id()
"""Put try/except to catch this value < 20k, from class above"""
emp_low.set_emp_salary(19000)
bonus = emp_low.calculate_bonus()
print("The current Employee details on bonus :")
print("Employee ID : ", emp_low.get_emp_id())
print("Salary :", emp_low.get_emp_salary())
print("Bonus :", bonus)
print("Total Salary :", bonus + emp_low.get_emp_salary())

