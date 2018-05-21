import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('WorldHappinessIndex.csv')
headers = df.columns.values 

print(headers)

rank = df.loc[0:,"Happiness Rank"]
score = df.loc[0:,"Happiness Score"]
capita_gdp = df.loc[0:,"Economy (GDP per Capita)"]
health = df.loc[0:,'Health (Life Expectancy)']
trust = df.loc[0:,'Trust (Government Corruption)']


score = (rank - rank.min())/rank.max()
capita_gdp = (capita_gdp - capita_gdp.min())/capita_gdp.max()
health = (health - health.min())/health.max()
trust = (trust- trust.min())/trust.max()

plt.plot(rank,score,label = 'Happines Score')
plt.plot(rank,capita_gdp,label = 'Per Capita GDP')
plt.plot(rank,health,label='Health (Life Expenctancy)')
plt.legend()
plt.xlabel('Happiness Rank')
plt.ylabel('Normalized Index')

plt.figure('Health vs GDP')
plt.plot(capita_gdp,trust)


plt.show()