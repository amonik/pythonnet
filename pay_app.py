import employee


def main():
    name = input("Please enter in your name: ")

    while True:
        try:
            designation_number = int(input("Please enter in \n1 for Director "
                                           "\n2 for Manager \n3 for Staff\n"))
            if 0 < designation_number <= 3:
                break
            print("Invalid number entered.")
        except Exception as e:
            print(e)

    while True:
        try:
            salary = float(input("Please enter in your salary: "))
            if salary <= 0:
                print("Your salary must be at least 1 dollar. Please enter a number greater than zero.")
            else:
                break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

    """Create Employee"""
    employee1 = employee.Employee()
    employee1.set_name(name)
    employee1.set_designation(designation_number)
    employee1.set_salary(salary)
    print(employee1.__str__())


if __name__ == '__main__':
    main()




