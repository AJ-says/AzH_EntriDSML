# Question 2: Employee Module

# Main.py
from Employee import Employee  # Importing Employee class from employee module

# Creating an Employee object
emp = Employee("Anjala Z Husain", 50000)
emp2 = Employee("Hyza Jazeel", 64000)

print("\n")
# Display Employee details
print(f"Employee1 - Name: {emp.get_name()} \t Salary: ${emp.get_salary()}")  
print(f"Employee2 - Name: {emp2.get_name()} \t Salary: ${emp2.get_salary()}")  
print("\n")