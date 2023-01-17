import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas_datareader import data
import sklearn.linear_model
# Load the data
start = '2020-04-01'
end = '2020-09-01'

df = data.DataReader('TSLA', 'yahoo', start, end)  # stock database
high = df['High'].to_numpy()
date = list(range(0, len(high)))
print(df)

#plotting
plt.xlabel("Date")
plt.ylabel("TSLA Stock Value")
plt.grid()
plt.scatter(date, high)
plt.show()
# Select a linear model
# model = sklearn.linear_model.LinearRegression()
# # Train the model
# model.fit(date, high)

# X_new = [[22587]]  
# print(model.predict(X_new))  
