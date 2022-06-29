import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import date
import re

req = requests.get("https://economictimes.indiatimes.com/indices/nifty_50_companies")
soup = BeautifulSoup(req.content,'html.parser')

products = []
dates = []
search_list = ['buy','target price','sell','rise']
today = date.today()
d1 = today.strftime('%d/%m/%Y')
for a in soup.findAll('a',href=True, attrs={'class':'semibold'}):
    texts = a.text
    
    if re.compile('|'.join(search_list),re.IGNORECASE).search(texts):
                                dates.append(d1)
                                products.append(a.text)

            
if not os.path.exists('C:/Users/Annamalai/Desktop/date_products.csv'):
                     df = pd.DataFrame({'Date':dates,'Stock Name':products}) 
                     df.to_csv('C:/Users/Annamalai/Desktop/date_products.csv', index=False, encoding='utf-8')
                     print('file created')

else:
    #print(products)
    df = pd.DataFrame({'Date':dates,'Stock Name':products})
 
    # append data frame to CSV file
    df.to_csv('C:/Users/Annamalai/Desktop/date_products.csv', mode='a', index=False, header=False)

    # print message
    print("Data appended successfully.")






