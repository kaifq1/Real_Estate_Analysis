#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("Real_Estate_Sales_2001-2021_GL.csv")


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


data.describe()


# In[7]:


threshold = len(data) * 0.5
data = data.dropna(thresh=threshold, axis=1)


# In[6]:


data.isnull().sum()


# In[8]:


plt.figure(figsize=(12, 6))
sns.boxplot(x=data['Sale Amount'], color='skyblue')


# In[9]:


sns.histplot(data['Sale Amount'], bins=50, kde=True)
plt.title('Distribution of Sale Amounts')
plt.xlabel('Sale Amount')
plt.ylabel('Frequency')
plt.show()


# In[22]:


plt.figure(figsize=(7, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[13]:


town_grouped = data.groupby('Town')['Sale Amount'].mean().reset_index()


# In[21]:


plt.figure(figsize=(7, 30))
sns.barplot(x='Sale Amount', y='Town', data=town_grouped.sort_values('Sale Amount', ascending=False), palette='viridis')
plt.title('Average Sale Amount by Town')
plt.xlabel('Average Sale Amount ($)')
plt.ylabel('Town')
plt.show()


# In[23]:


data['Date Recorded'] = pd.to_datetime(data['Date Recorded'])


# In[24]:


data['Year'] = data['Date Recorded'].dt.year


# In[25]:


yearly_sales = data.groupby('Year')['Sale Amount'].sum().reset_index()


# In[27]:


plt.figure(figsize=(9, 4))
sns.lineplot(x='Year', y='Sale Amount', data=yearly_sales, marker='o')
plt.title('Total Sale Amount by Year')
plt.xlabel('Year')
plt.ylabel('Total Sale Amount ($)')
plt.show()


# This project analyzed real estate sales data from 2001 to 2021, revealing key trends, correlations, and market variations across different towns.
