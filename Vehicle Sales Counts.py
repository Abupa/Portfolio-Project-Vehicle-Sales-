#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[131]:


data = pd.read_csv('MVA_Vehicle_Sales_Counts_by_Month_for_Calendar_Year_2002_through_December_2023.csv')
data.columns = data.columns.str.strip()
print(data.head(10))


# In[132]:


print(data.info())


# In[133]:


print(data.describe())


# In[134]:


data['Sales difference'] = data['Total Sales New'] - data['Total Sales Used']
print(data.head(10))
#This difference suggests that new cars generate more income than used cars. Even though used cars were sold in larger quantities.


# In[138]:


data['Aggregated'] = data['New'] + data['Used']
profitable_month = data.groupby('Month')['Aggregated'].sum()
print(profitable_month)


# In[142]:


profitable_month.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Aggregated Sales by Month')
plt.xticks(rotation=45) 
plt.show()
#As we can see, from the beginning of autumn there is a decline in sales that lasts until the end of winter. And with the onset of spring and until the end of summer, sales grow and remain at a similar pace. All this tells us that people prefer to shop during these times of year.


# In[144]:


n = 1
t = 2
d = 20
w = 0.8

data_subset = data[:20]

x_values1 = [t * element + w * n for element in range(d)]
plt.bar(x_values1, data_subset['New'], label = 'New Cars')

n = 2
x_values2 = [t * element + w * n for element in range(d)]
plt.bar(x_values2, data_subset['Used'], label = 'Used Cars')

plt.ylabel('Number of cars sold')
plt.title('Comparison of new and used car sales')
plt.legend()
plt.show()


# In[146]:


plt.figure(figsize=(10, 6))

plt.plot(data['Year'], data['New'], marker='o', label='New')
plt.plot(data['Year'], data['Used'], marker='o', label='Used')

plt.title('Number of New and Used Vehicles Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.legend()

plt.grid(True)
plt.show()
#As we can see, people prefer to buy used cars rather than new ones.


# In[ ]:




