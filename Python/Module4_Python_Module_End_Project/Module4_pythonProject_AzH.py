import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Python/myexcel.csv")  # Replace with actual filename

# Preprocessing: Replace 'Height' column with random values between 150 and 180
df["Height"] = np.random.randint(150, 181, df.shape[0])

# Analysis Task 1: Employee distribution across teams
team_distribution = df["Team"].value_counts()
team_percentage = (team_distribution / df.shape[0]) * 100

team_analysis_df = pd.DataFrame({
    "Team": team_distribution.index,
    "Employee Count": team_distribution.values,
    "Percentage": team_percentage.values
})

print("\nTeam Distribution Analysis:")
print(team_analysis_df)

# Visualization: Team distribution
plt.figure(figsize=(12, 6))
sns.barplot(x=team_distribution.index, y=team_distribution.values, palette="viridis")
plt.xlabel("Teams")
plt.ylabel("Number of Employees")
plt.title("Employee Distribution Across Teams")
plt.xticks(rotation=45, ha="right")
plt.tight_layout
plt.show()

# Analysis Task 2: Employee distribution across positions
position_distribution = df["Position"].value_counts()
position_analysis_df = pd.DataFrame({
    "Position": position_distribution.index,
    "Employee Count": position_distribution.values
})

print("\nPosition Distribution Analysis:")
print(position_analysis_df)

# Visualization: Position distribution
plt.figure(figsize=(10, 5))
sns.barplot(x=position_distribution.index, y=position_distribution.values, palette="viridis")
plt.xlabel("Positions")
plt.ylabel("Number of Employees")
plt.title("Employee Distribution Across Positions")
plt.show()

# Analysis Task 3: Identify predominant age group
age_bins = [20, 25, 30, 35, 40, 45, 50]
age_labels = ["20-25", "26-30", "31-35", "36-40", "41-45", "46-50"]
df["Age Group"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels, right=False)
age_group_distribution = df["Age Group"].value_counts()

print("\nAge Group Distribution Analysis:")
print(age_group_distribution)

# Visualization: Age group distribution
plt.figure(figsize=(8, 5))
sns.barplot(x=age_group_distribution.index, y=age_group_distribution.values, palette="viridis")
plt.xlabel("Age Groups")
plt.ylabel("Number of Employees")
plt.title("Age Group Among Employees")
plt.show()

# Analysis Task 4: Team and Position with highest salary expenditure
team_salary = df.groupby("Team")["Salary"].sum().reset_index().sort_values(by="Salary", ascending=False)
position_salary = df.groupby("Position")["Salary"].sum().reset_index().sort_values(by="Salary", ascending=False)

print("\nTeam Salary Expenditure Analysis:")
print(team_salary)

print("\nPosition Salary Expenditure Analysis:")
print(position_salary)

# Visualization: Salary expenditure by team
plt.figure(figsize=(12, 6))
sns.barplot(x=team_salary["Team"], y=team_salary["Salary"], palette="viridis")
plt.xlabel("Teams")
plt.ylabel("Total Salary Expenditure")
plt.title("Total Salary Expenditure by Team")
plt.xticks(rotation=45, ha="right")
plt.tight_layout
plt.show()

# Visualization: Salary expenditure by position
plt.figure(figsize=(10, 5))
sns.barplot(x=position_salary["Position"], y=position_salary["Salary"], palette="viridis")
plt.xlabel("Positions")
plt.ylabel("Total Salary Expenditure")
plt.title("Total Salary Expenditure by Position")
plt.show()

# Analysis Task 5: Correlation between Age and Salary
correlation_value = df["Age"].corr(df["Salary"])
print(f"\nCorrelation between Age and Salary: {correlation_value:.4f}\n")

# Visualization: Correlation between Age and Salary
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df["Age"], y=df["Salary"], color="green")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Correlation between Age and Salary")
plt.grid(True)
plt.show()
