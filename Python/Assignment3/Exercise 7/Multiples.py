# Exercise 7

num = int(input("\nEnter a number: "))
limit = int(input("Enter the limit: "))

print(f"First {limit} Multiples of {num}:")
for i in range(1, limit+1):
    print("\t", num * i, end=" ")
print("\n")
