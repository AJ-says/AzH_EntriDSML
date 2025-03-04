# Exercise 3

weight = float(input("\nEnter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal"
elif 25 <= bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print(f"You are in the \"{status}\" range.\n")
