import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
file = open(os.path.expanduser("Nutrition.csv"),'wb')

url = "http://www.hc-sc.gc.ca/fn-an/nutrition/fiche-nutri-data/nutrient_value-valeurs_nutritives-tc-tm-eng.php"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
header = 'Food Name , Measure , Weight (g) , Energy (kcal) , Energy (kJ) , Protein (g) , Carbohydrate (g) , Total Sugar (g) , Total Dietary Fibre (g) , Total Fat (g) , Saturated Fat (g) , Cholesterol (mg) , Calcium (mg) , Iron (mg) , Sodium (mg) , Potassium (mg) , Magnesium (mg) , Phosphorus (mg) , Thiamin (mg) , Riboflavin (mg) , Niacin (NE) , Folate (DFE)'+'\n'
file.write(bytes(header,encoding="ascii", errors='ignore'))
for row in soup.findAll('tr'):
    rowdata = ""
    for cell in row.findAll('td'):
        cell = str(cell.text)
        cell = cell.replace(',','-')
        rowdata = rowdata + cell + ','
    if(len(rowdata)>25):
        rowdata+= '\n'
        file.write(bytes(rowdata,encoding="ascii", errors='ignore'))
        print(rowdata)