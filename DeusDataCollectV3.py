from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time


index=str(input('index: '))


start = time.time()  # code timer
i = 1
numdata = 5  # number of data entries collected
delay = 1  # seconds between each data collection
data = []
link = "https://www.google.com/finance/quote/{}:NASDAQ?hl=en".format(index) #change link from NADAQ to different stock exchange for non NASDAQ stocks
page = requests.get(link)
html_page = page.content
soup = bs(html_page, 'html.parser')  # html garbage
text = str(soup.find_all("div", {"class": "YMlKec fxKbKc"}))

while i<numdata:
    loc = text.find('$') # first character before price
    loc2= text.find("<", loc) #last character after price
    price = text[loc:loc2]  # current stock price (can use loc+1 if we want to remove the $ for data)
    data.append(price)
    i = i+1
    time.sleep(delay)

print(data)
print(time.time()-start)
