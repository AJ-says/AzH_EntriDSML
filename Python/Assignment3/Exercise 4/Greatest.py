# Exercise 4

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

numbers = [num1, num2, num3]

greatest = numbers[0]  # Assume the first number is the greatest

for num in numbers:
    if num > greatest:
        greatest = num

print(f"The greatest number is: {greatest}\n")
