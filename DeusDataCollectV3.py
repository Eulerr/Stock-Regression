from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time
import datetime 


index=str(input('index: '))


start = time.time()  # code timer
i = 0
numdata = 5  # number of data entries collected
delay = 1  # seconds between each data collection
prices = []
dates = []
link = "https://www.google.com/finance/quote/{}:NASDAQ?hl=en".format(index) #change link from NAsDAQ to different stock exchange for non NASDAQ stocks
while i < numdata:
    #code to find stock price from website HTML (Adds ~0.5 secs per itteration due to requests.get(link) line.... faster method??) faster_than_requests module
    page = requests.get(link)
    html_page = page.content
    soup = bs(html_page, 'html.parser')  # html garbage
    text = str(soup.find_all("div", {"class": "YMlKec fxKbKc"}))
    
    #code to make put stock price in a list
    loc = text.find('$') # first character before price
    loc2 = text.find("<", loc) #last character after price
    price = text[loc+1:loc2]  # current stock price 

    date = str(datetime.datetime.now())
    dates.append(date) 
    prices.append(price)
    i = i+1
    time.sleep(delay)
        

print(prices)
print(dates)
print(time.time()-start)

#data_titles= ["Time", "{} Stock Price".format(index)]
#data = list(zip(dates, prices))
data= { 'Time': dates, '{} Stock Price'.format(index):prices}
df= pd.DataFrame(data)
print(df)