# Question 2: Employee Module

# Employee.py
class Employee:
    """Class representing an employee with name and salary attributes"""
    
    def __init__(self, name, salary):
        """Initialize Employee attributes"""
        self.name = name
        self.salary = salary

    def get_name(self):
        """Returns employee name"""
        return self.name

    def get_salary(self):
        """Returns employee salary"""
        return self.salary
