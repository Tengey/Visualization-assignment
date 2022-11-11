# -*- coding: utf-8 -*-

"""
Created on Fri Nov 11 17:55:55 2022

@author: Owner
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# reading csv file into spyder using pandas
df = pd.read_csv('cause_of_deaths.csv')

# printing first 5 rows from my data frame
print(df.head())
print('\n')

# printing data types in df
print(df.dtypes)
print('\n')

# printing the sum of all nulls in df
print(df.isnull().sum())
print(df)


# plotting bar chart of Meningitis mortality rate in Ghana & the UK
country_a = mpatches.Patch(color='blue', label='Ghana')
country_b = mpatches.Patch(color='orange', label='United Kingdom')
plt.plot(df[df['Country/Territory'] == 'Ghana']['Year'],
         df[df['Country/Territory'] == 'Ghana']['Meningitis'])

plt.plot(df[df['Country/Territory'] == 'United Kingdom']['Year'],
         df[df['Country/Territory'] == 'United Kingdom']['Meningitis'])

plt.title('Meningitis Mortality Rate In Ghana & The UK')
plt.legend(handles=[country_a, country_b])
plt.tight_layout()


# line plot showing 10 countries affected by Meningitis
data = df.groupby('Country/Territory')['Meningitis'].sum().reset_index()
data = data.sort_values(by = 'Meningitis',  ascending = False)
fig, ax = plt.subplots()
ax.barh(data['Country/Territory'][:10], data['Meningitis'][:10])
plt.xticks(rotation = 90)
plt.ylabel('cause of deaths')
plt.xlabel('Country')
plt.title('Top 10 Countries affected by Meningitis')
plt.show()


print('\n')
# plotting pie chart of ten countries affected by Malaria
data_2 = df.groupby('Country/Territory')['Malaria'].sum().reset_index()
data_2 = data_2.sort_values(by = 'Malaria', ascending = False)
size = []
for y in data_2['Malaria']:
    size.append(y)
name = []
for i in data_2['Country/Territory']:
    name.append(i)
explode = (0, 0.1)
plt.figure()
plt.pie(size[:10], labels = name[:10])
plt.title('Top ten countries affected by Malaria')  
plt.tight_layout()

