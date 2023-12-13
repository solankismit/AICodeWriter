
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Salary_Data.csv')

# Split the data into independent and dependent variables
x = data['YearsExperience']
y = data['Salary']

# Fit the linear regression model
model = np.polyfit(x, y, 1)

# Plot the data and the regression line
plt.scatter(x, y)
plt.plot(x, model, color='red')
plt.show()

# Print the coefficients of the regression line
print(model)
