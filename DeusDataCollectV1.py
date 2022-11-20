# Importing Libraries
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time
#pulling website
page = requests.get("https://www.google.com/finance/quote/TSLA:NASDAQ?hl=en") #website
html_page=page.content
soup=bs(html_page, 'html.parser')#html garbage
text=soup.find_all(text=True)
output = ''
blacklist = ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script',] #list of html elements to exclude

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t) #website text

#collecting data from output and storing it
index=output.find('Tesla Inc $') #index of Tag before stock price
i=1  
numdata=5 #number of data entries collected
delay=0 #seconds between each data collection
data=[]
while i <= numdata: #collects stock data over time and stores it in variable
    price= output[index+11:index+18] #current stock price
    data.append(price)
    i=i+1
    time.sleep(delay)
    
print(data)

#next collect data in a DF using pandas collecting stock name and date and time with every price
