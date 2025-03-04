import numpy as np
import pandas as pd

# Exercise 1: Create and Reshape Numpy Array 
arr1 = np.arange(1, 11).reshape(2, 5)
print("\nExercise 1: 2x5 Matrix\n",arr1)

# Exercise 2: Extract Elements from Numpy Array 
arr2 = np.arange(1, 21)
extracted_elements = arr2[5:16]
print("\nExercise 2: Extracted Elements\n",extracted_elements)

# Exercise 3: Create and Modify Pandas Series 
fruit_series = pd.Series({'apples': 3, 'bananas': 2, 'oranges': 1})
fruit_series['pears'] = 4
print("\nExercise 3: Updated Pandas Series\n",fruit_series)

# Exercise 4: Create DataFrame
data = {
    "name": ["Anjala", "Jazeel", "Amal", "Hyza", "Jaseem", "Shaheen", "Faeza", "Fayha", "Eesa", "Pathu"],
    "age": [25, 30, 22, 45, 29, 33, 26, 40, 38, 27],
    "gender": ["Female", "Male", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female"]
}

df = pd.DataFrame(data)
print("\nExercise 4: DataFrame\n",df)

# Exercise 5: Add New Column to DataFrame
df["occupation"] = ["Programmer", "Manager", "Analyst", "Manager", "Programmer",
                    "Analyst", "Manager", "Programmer", "Analyst", "Manager"]
print("\nExercise 5: DataFrame with Occupation Column\n",df)

# Exercise 6: Select Rows with Age >= 30 
df_filtered = df[df["age"] >= 30]
print("\nExercise 6: Rows where Age >= 30\n",df_filtered)

# Exercise 7: Convert DataFrame to CSV and Read Back
csv_filename = "Python/Ass07_AzH/dataframe_output.csv"
df.to_csv(csv_filename, index=False)

# Read the CSV file
df_read = pd.read_csv(csv_filename)
print("\nExercise 7: Read CSV File Content\n",df_read)

# Display the final dataframe to user
print("\nFinal DataFrame\n",df_read, "\n")