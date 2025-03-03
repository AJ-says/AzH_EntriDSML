

# Exercise 1: Print name, student number, and email
print("\nExercise 1: Print name, student number, and email")
print("Anjala ST1001 anjuzh@gmail.com")

# Exercise 2: Print using escape sequences
print("\nExercise 2: Print using escape sequences")
print("\tAnjala \n ST1001 \n anjuz@gmail.com \n")

# Exercise 3: Perform basic arithmetic operations
print("\nExercise 3: Perform basic arithmetic operations")
num1 = 14
num2 = 7
print(f"\t{num1} + {num2} = {num1 + num2}")
print(f"\t{num1} * {num2} = {num1 * num2}")
print(f"\t{num1} - {num2} = {num1 - num2}")
print(f"\t{num1} / {num2} = {num1 / num2}")

# Exercise 4: Display numbers 1 to 5 as steps
print("\nExercise 4: Display numbers 1 to 5 as steps")
print("\n1\n\t2\n\t\t3\n\t\t\t4\n\t\t\t\t5\n")

# Exercise 5: Print a sentence with quotation marks
print("\nExercise 5: Print a sentence with quotation marks")
print("\"SDK\" stands for \"Software Development Kit\", whereas \"IDE\" stands for \"Integrated Development Environment\".")

# Exercise 6: Practice and check the output
print("\nExercise 6: Practice and check the output")
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")
print()

# Exercise 7: Define variables, display Types and find Sum
print("\nExercise 7: Define variables, display Types and find Sum")
num = 23
textnum = "57"
decimal = 98.3
print(f"Variable Datatypes:\n\t num:{num,type(num)}\n\t textnum:{textnum,type(textnum)}\n\t decimal:{decimal,type(decimal)}")
total_sum = num + int(textnum) + decimal
print(f"Sum: {total_sum}")
print(f"Datatype of sum: {type(total_sum)}")

# Exercise 8: Calculate minutes in a year
print("\nExercise 8: Calculate minutes in a year")
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
total_minutes = days_in_year * hours_in_day * minutes_in_hour
print("Created three variables to store no of days in a year, minute in a hour, hours in a day,\nthen calculate the total minutes in a year and print the values \n (hint) total number of minutes in an year = No.of days in an year * Hours in a day * Minutes in an hour ")
print(f"Total number of minutes in a year: {total_minutes}")

# Exercise 9: Ask for name and print greeting
print("\nExercise 9: Ask for name and print greeting\n")
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

# Exercise 10: Convert Pounds to Dollars
print("\nExercise 10: Convert Pounds to Dollars\n")
pounds = float(input("Please enter amount in pounds: "))
dollar_rate = 1.26  # Exchange rate
usd = pounds * dollar_rate
print(f"£{pounds} is ${usd:.2f}\n")
