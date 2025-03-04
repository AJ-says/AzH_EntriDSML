import matplotlib.pyplot as plt
import seaborn as sns

# Exercise 1: Line Plot for City Population 
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]

city_a_population = [500000, 550000, 600000, 650000, 700000, 750000, 800000]
city_b_population = [800000, 850000, 900000, 950000, 1000000, 1050000, 1100000]
city_c_population = [1000000, 1050000, 1100000, 1150000, 1200000, 1250000, 1300000]
city_d_population = [1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000]

plt.figure(figsize=(10, 5))
plt.figure(figsize=(10, 5))
plt.plot(years, city_a_population, marker='o', color="red", label="City A")   
plt.plot(years, city_b_population, marker='s', color="magenta", label="City B")  
plt.plot(years, city_c_population, marker='^', color="pink", label="City C") 
plt.plot(years, city_d_population, marker='d', color="purple", label="City D")


plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Exercise 1 - Population Growth of Cities Over Time")
plt.legend()
plt.grid(True)
plt.show()

# Exercise 2: Scatter Plot for Hours Studied vs. Test Scores 
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [93, 57, 61, 54, 51, 53, 87, 81, 83, 85]

plt.figure(figsize=(8, 5))
sns.scatterplot(x=hours_studied, y=test_scores, color='red')
plt.xlabel("Hours Studied")
plt.ylabel("Test Scores")
plt.title("Exercise 2 - Relationship Between Hours Studied and Test Scores")
plt.grid(True)
plt.show()

# Exercise 3: Bar Chart for Monthly Sales
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [11860, 10480, 4997, 5523, 13965, 6011, 13158, 9533, 5158, 9058, 11346, 6675]

plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='purple')

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Exercise 3 - Total Sales Per Month")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
