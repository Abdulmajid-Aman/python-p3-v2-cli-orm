from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    print('Here are all the Departments')
    departments = Department.get_all()
    
    for department in departments:
        print(f"Name: {department.name} Location: {department.location} Id: {department.id}")


def find_department_by_name():
    user_input = input('Enter the Department name: > ')
    department = Department.find_by_name(user_input)
    if department:
        print("Here is your searched Department")
        print(f"{department.name} {department.location} {department.id}")
    else:
        print('No search was found')


def find_department_by_id():
    user_input = input("Enter Department ID > ")
    department = Department.find_by_id(user_input)
    if department:
        print("Here is your searched Department")
        print(f"{department.name} {department.location} {department.id}")
    else:
        print('No search was found')

def create_department():
    department_name = input("Enter department name")
    department_location = input('Enter department location')
    Department.create(name=department_name, location=department_location)
    print("Department created")

def update_department():
    department_id = input("Enter Department ID ")
    department = Department.find_by_id(department_id)

    if department:
        new_name = input("Enter new company name ")
        new_location = input('Enter new company location ')
        if new_name:
            department.name = new_name
        else:
            print("No name was entered")
        if new_location:
            department.location = new_location
        else:
            print('No new location was entered')
    print(f"{department.name} - {department.location}")
    




def delete_department():
    department_id = input("Enter Department ID ")

    department = Department.find_by_id(department_id)
    if department:
        department.delete()
        print('Department has been deleted')
    else:
        print('No department has been found')
    


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(f"Name: ({employee.name}) Job_Title: ({employee.job_title})")


def find_employee_by_name():
    employee_name = input('Enter employee name ')
    employee = Employee.find_by_name(employee_name)
    if employee:
        print('Employee found. Here are the details about him / her')
        print(f"Name: ({employee.name}) Job_Title: ({employee.job_title})")
    else:
        print('No employee has been found')


def find_employee_by_id():
    employee_id = input('Enter employee ID')
    employee = Employee.find_by_id(employee_id)
    if employee:
         print('Employee found. Here are the details about him / her')
         print(f"Name: ({employee.name}) Job_Title: ({employee.job_title})")
    else:
        print('No employee has been found')


def create_employee():
    employee_name = input('Enter employee name')
    employee_jobTitle = input('Enter employee Job title')
    employee_id = int(input('Enter department id'))
    Employee.create(name = employee_name, job_title = employee_jobTitle, department_id = employee_id )
    print('Employee has been created')


def update_employee():
    employee_id = input('Enter employee id')
    employee = Employee.find_by_id(employee_id)

    if employee:
        name = input('Enter new name')
        job_title = input('Enter job title')
        if name:
            employee.name = name
        else:
            print('No name was entered')
        if job_title:
            employee.job_title = job_title
        else:
            print('No new job title has been entered')
    employee.save()

    print(f"({employee.name}) - ({employee.job_title})")


def delete_employee():
    id = input('Enter Employee id')

    employee = Employee.find_by_id(id)
    employee.delete()
    print('Employee deleted')


def list_department_employees():
    id = input('Enter department id')
    department = Department.find_by_id(id)
    if department:
        employees = department.employees()
        if employees:
            for employee in employees:
                print(f"Name: ({employee.name}) Job_Title: ({employee.job_title})")
        else:
            print('No employees have been found')
    else:
        print('No department found')