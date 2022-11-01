import csv
from bs4 import BeautifulSoup
import requests

url = "https://finance.yahoo.com/currencies?.tsrc=fin-srch"
req = requests.get(url)
print(req)
req.encoding = "utf-8"
soup = BeautifulSoup(req.text, "html.parser")




euro_list = []

change_data = soup.find_all('fin-streamer',{'data-symbol':'EURUSD=X'})
for i in change_data:
    euro_list.append(i.string)

print(euro_list[0])


course_list = []





