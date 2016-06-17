#fetching temperature from google data

import requests
from bs4 import*
import time
city = input("Enter the name of the city :  ")
city=city.lower()
url="https://www.google.co.in/search?q=weather+"+city
data = requests.get(url)
soup=BeautifulSoup(data.text,"html.parser")
data2 = soup.find_all('div')
data2= soup.findAll('span',{'class':'wob_t'})

print(data2[0].contents[0])


time.sleep(5)











## fetching from accuweather
'''

data = requests.get("http://www.accuweather.com/en/in/mumbai/204842/weather-forecast/204842")
soup = BeautifulSoup(data.text,"html.parser")
data2 = soup.find('div',{"class":"info"})
data3 = data2.find('strong',{"class":"temp"})
print(data3.contents[0])
'''