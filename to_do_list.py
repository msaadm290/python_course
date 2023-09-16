employees = []

salary_deposited_employees = []

def add_emp(emp):
    employees.append(emp)
    print("Employes added",emp)


def list_employees():
    if not employees:
       print("No employees found")
    else:   
      print("Name of Employees:")
      for i,emp in enumerate(employees,start=1):
        print(f"{i}, {emp}")


def list_salary_deposited_employees():
    if not salary_deposited_employees:
       print("No salary deposited employees found")
    else:   
      print("Names of all salary deposited employees:")
      for i,emp in enumerate(salary_deposited_employees,start=1):
        print(f"{i}, {emp},deposited")        


def salary_deposited(emp_index):
   if 1 <=emp_index <=len(employees):
    emp = employees[emp_index - 1]
    print(f"Salary deposited:, {emp}")
    salary_deposited_employees.append(emp)
    employees.pop(emp_index-1)
    #employees.copy[emp_index]
   else:
    print("invalid employe index")


def employee_delete(emp_index):
   if 1 <= emp_index <= len(employees):
    emp = employees[emp_index - 1]
    print(f"Employee deleted: {emp}")
    employees.pop(emp_index - 1)
    #employees.sort(emp_index)
   else:
    print("Invalid employee index.")
    

while True:
   print("options")
   print("Enter 'add_emp' to add a employees")
   print("Enter 'list_employees' to list all employees")
   print("Enter 'list_salary_deposited_employees' all deposited employees")
   print("Enter 'salary_deposited' to mark as deposited")
   print("Enter 'employee_delete' to mark as deleted")
   print("Enter 'quite' to exit the program")

   #user_input = input("chose a option").lower()
   user_input = input("chose a option").lower().strip()

   if user_input == "quite":    
    break
   elif user_input == "add_emp":
    emp = input("Enter a employee name:")
    add_emp(emp)
   elif user_input == "list_employees":
    list_employees()
   elif user_input == "list_salary_deposited_employees":
    list_salary_deposited_employees() 
   elif user_input == "salary_deposited":
    emp = int(input("Enter the employee number to mark as salary deposited"))
    salary_deposited(emp)
   elif user_input == "employee_delete":
     emp = int(input("Enter the employe number to delete:"))
     employee_delete(emp)

   else:
    print("Invalid input. please try again")   


  #option mai , kar k fill karaingay.
  #if only 1 employee just use it other wise use the loop condition pher us mai append ho ga or may be spilit be use ho ga.

