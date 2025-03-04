# Exercise 5

num = int(input("\nEnter a number: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.\n")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}\n")
