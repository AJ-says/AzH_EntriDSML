

# Question 1:
# The len() function in Python returns the number of elements in a sequence (e.g., list, string, tuple, etc.)
# Example: Finding the length of a list
print("\nQuestion 1:")
numbers = [10, 20, 30, 40, 50]
print("Length of the list:", len(numbers))  



# Question 2: Function to greet a user by name
print("\nQuestion 2:")
def greet(name):
    print(f"Hello, {name}!")
# Function Call
greet("Anjala ZH") 



# Question 3: Function to find the maximum number in a list without using max()
print("\nQuestion 3:")
def find_maximum(numbers):
    if not numbers: 
        return None
    max_value = numbers[0]  
    for num in numbers[1:]:  
        if num > max_value:
            max_value = num
    return max_value
# Function Call
num_list = [3, 7, 2, 9, 5]
print("Maximum value:", find_maximum(num_list)) 



# Question 4: Local vs. Global Variables in Functions
print("\nQuestion 4:")
x = 10  # Global variable
def example_function():
    x = 5  # Local variable (only exists inside this function)
    print("Inside function, x =", x) 
# Calling function
example_function()
print("Outside function, x =", x) 
# A local variable is confined within the function, while a global variable exists throughout the program.
# If both have the same name, Python prioritizes the local variable inside the function, keeping the global variable unchanged outside.



# Question 5: Function to calculate the area of a rectangle with a default width
print("\nQuestion 5:")
def calculate_area(length, width=5):
    return length * width
# Function Call
print("Area with length=10 and default width:", calculate_area(10)) 
print("Area with length=10 and width=8:", calculate_area(10, 8), "\n")  
