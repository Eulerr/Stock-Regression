import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import numpy as np

# start=input("enter start date (yyyy, mm, dd):  ")
# end=input("enter end date (yyyy, mm, dd): ")

start= '2012, 4, 1'
end= '2012, 9, 1'

#data collection
df=pdr.DataReader('tsla', 'yahoo', start, end)#stock database
high=df['High'].to_numpy()
date= list(range(0,len(high)))
m,b=np.polyfit(date, high,1)#line of best fit
y = []
for i in range(len(date)):
    y.append(m*date[i]+b)
    
#plotting
plt.scatter(date,high)
plt.plot(date, y)
plt.show()





