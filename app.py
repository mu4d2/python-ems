# Simple EMS using lists' methods and functions

employees = ["Hamid", "Sara", "Robert", "Lee Wah", "Rami"]

while True:
    print("""
        Welcome to Employees Management System!

        Available command:
        -> add      : to add employee
        -> delete   : to remove employee
        -> view     : to view all employees
        -> check    : to check whether an employee exists
        -> quit     : to exit the app
    """)

    command = input("Select your command: ")
    
    if command == "add":
        addEmployee = input("Please enter employee's name you want to add: ")
        employees.append(addEmployee)
        print("Latest employees list =>", employees)
    elif command == "delete":
        deleteEmployee = input("Please enter employee's name you want to delete: ")
        employees.remove(deleteEmployee)
        print("Latest employees list =>", employees)
    elif command == "view":
        print(employees)
    elif command == "check":
        checkEmployee = input("Please enter employee's name you want to check: ")
        if checkEmployee in employees:
            print("Yes,", checkEmployee, "is in the record.")
        else:
            print(checkEmployee, "is not in your record.")
    elif command == "quit":
        break