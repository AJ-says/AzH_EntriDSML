# Exercise 1

month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

month = int(input("\nEnter the month: "))

if 1 <= month <= 12:
    print(f"Month {month} is {month_names[month - 1]}\n")
else:
    print("Invalid month! Please enter a number between 1 and 12.\n")
