import random

# Topic: List
# Q1: Create a list of 5 random numbers and print the list
random_list = [random.randint(1, 100) for _ in range(5)]
print("\nList:", random_list)

# Q2: Insert 3 new values to the list and print the updated list
random_list.extend([500, 320, 145])
print("Updated List:", random_list)

# Q3: Use a for loop to print each element in the list
print("Elements in the List:")
for item in random_list:
    print("\t",item)

# Topic: Dictionary
# Q1: Create a dictionary with keys 'name', 'age', and 'address'
info_dict = {"name": "John", "age": 25, "address": "New York"}
print("\nDictionary:", info_dict)

# Q2: Add a new key-value pair to the dictionary
info_dict["phone"] = "1234567890"
print("Updated Dictionary:", info_dict)

# Topic: Set
# Q1: Create a set with values 1, 2, 3, 4, and 5
num_set = {1, 2, 3, 4, 5}
print("\nSet:", num_set)

# Q2: Add the value 6 to the set
num_set.add(6)
print("Updated Set [after adding 6]:", num_set)

# Q3: Remove the value 3 from the set
num_set.discard(3)
print("Updated Set [after removing 3]:", num_set)

# Topic: Tuple
# Q1: Create a tuple with values 1, 2, 3, and 4
num_tuple = (1, 2, 3, 4)
print("\nTuple:", num_tuple)

# Q2: Print the length of the tuple
print("Length of Tuple:", len(num_tuple), "\n")
