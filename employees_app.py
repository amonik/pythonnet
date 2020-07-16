from customers import Employee
from custom_exception import NotEnough, IsNegative

# Employee with at least 20,000 and if not exception is raised.
emp_good = Employee('Stephanie', 'Tian')
emp_good.set_emp_id()
while True:
    try:
        pay = float(input("Please enter in your pay: "))
        break
    except ValueError:
        print("Must be a number.")
try:
    emp_good.set_emp_salary(pay)
# Call the custom Exception.
except NotEnough as error:
    print(error)
except IsNegative as error:
    print(error)
bonus = emp_good.calculate_bonus()
print("The current Employee details on bonus :")
print(emp_good.get_name())
print("Employee ID : ", emp_good.get_emp_id())
print("Salary :", emp_good.get_emp_salary())
print("Bonus :", bonus)
print("Total Salary :", bonus + emp_good.get_emp_salary())


