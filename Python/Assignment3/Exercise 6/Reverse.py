# Exercise 6

num = int(input("\nEnter a number: "))
rev_num = 0

while num > 0:
    rev_num = (rev_num * 10) + (num % 10)
    num //= 10

print(f"Reversed number: {rev_num}\n")
