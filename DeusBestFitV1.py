import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

# start=input("enter start date (yyyy, mm, dd):  ")
# end=input("enter end date (yyyy, mm, dd): ")

yf.pdr_override() 

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
high=data['High'].to_numpy()
date= list(range(0,len(high)))
m,b=np.polyfit(date, high,1)#line of best fit
y = []
for i in range(len(date)):
    y.append(m*date[i]+b)
    
#plotting
plt.xlabel("Date")
plt.ylabel("TSLA Stock Value")
plt.grid()
plt.scatter(date,high)
plt.plot(date, y)
plt.show()






