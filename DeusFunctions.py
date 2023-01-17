import matplotlib as plt
import pandas as pd
import pandas_datareader as pdr

def graphdata(x,y):
    start=x
    end=y

    df = pdr.DataReader('tsla', 'yahoo', start, end)  # stock database
    high = df['High'].to_numpy()
    date = list(range(0, len(high)))

    #plotting
    plt.xlabel("Date")
    plt.ylabel("TSLA Stock Value")
    plt.grid()
    plt.scatter(date, high)
    plt.plot(date, y)
    plt.show()
    return(date, high)
    
