 # Exercise 1: Read a file and display its contents
print("\nExercise 1: Read a file and display its contents")
filename = "Python/Ass05_AzH/SampleFile.txt" 
with open(filename, "r") as file:
    content = file.read()
print("File Contents:\n\t", content)



# Exercise 2: Copy contents of one file to another
print("\nExercise 2: Copy contents of one file to another")
source_file = "Python/Ass05_AzH/SampleFile.txt" 
destination_file = "Python/Ass05_AzH/SampleFile_copy.txt" 
with open(source_file, "r") as src, open(destination_file, "w") as dest:
    dest.write(src.read())
print(f"Contents copied from {source_file} to {destination_file}")



# Exercise 3: Count the total number of words in a file
print("\nExercise 3: Count the total number of words in a file")
with open(filename, "r") as file:
    content = file.read()
    word_count = len(content.split()) 
    print(f"Total number of words in '{filename}': {word_count}")



# Exercise 4: Convert string input to integer with exception handling
print("\nExercise 4: Convert string input to integer with exception handling")
while True:
    try:
        user_input = input("Enter a number: ")
        num = int(user_input)
        print(f"Converted integer: {num}")
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
    exe = input("Would you like to try again? ('yes' to continue, 'no' to move to the next exercise): ").strip().lower()
    if exe == "no":
        break



# Exercise 5: Check for negative numbers in a user-inputted list
print("\nExercise 5: Check for negative numbers in a user-inputted list")
while True:
    try:
        numbers = list(map(int, input("Enter a list of integers (separated by spaces): ").split()))
        for num in numbers:
            if num < 0:
                raise ValueError("Negative numbers are not allowed.")
        print("Valid list:", numbers)
    except ValueError as e:
        print(f"Error: {e}")
    exe = input("Would you like to try again? ('yes' to continue, 'no' to move to the next exercise): ").strip().lower()
    if exe == "no":
        break



# Exercise 6: Compute average and handle exceptions
print("\nExercise 6: Compute average and handle exceptions")
while True:
    try:
        numbers = list(map(int, input("Enter a list of integers (separated by spaces): ").split()))
        avg = sum(numbers) / len(numbers)
        print(f"Average: {avg:.2f}")
    except ZeroDivisionError:
        print("Error: Cannot calculate the average of an empty list.")
    except ValueError:
        print("Error: Please enter valid integers.")
    finally:
        print("Program execution completed.")
    exe = input("Would you like to try again? ('yes' to continue, 'no' to move to the next exercise): ").strip().lower()
    if exe == "no":
        break



# Exercise 7: Write a string to a file and handle exceptions
print("\nExercise 7: Write a string to a file and handle exceptions")
filename = input("Enter the filename: ")
try:
    with open(filename, "w") as file:
        file.write("Welcome to Python File Handling!")
    print("File written successfully!")
except Exception as e:
    print(f"An error occurred: {e}\n")
else:
    print("Welcome! No errors occurred.\n")
print("\n")