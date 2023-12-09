#!/usr/bin/env python
# coding: utf-8

# # Consumer Behavior in eCommerce 
# 
# We can try to analyze the data to understand age, and purchase dollar amount. We can see the general trends in spending in electronics, books and clothing (qualitative shopping category removed for ease of box plots) by age, purchase amount and quantity. 
# 
# Data source: https://www.kaggle.com/datasets/shriyashjagtap/e-commerce-customer-for-behavior-analysis?select=ecommerce_customer_data_custom_ratios.csv

# ### A)  Data Columns & Info 

# In[7]:


#Importing cvs file in consumer analytics 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('eCommerce customer data.csv')


# In[8]:


#We want to see the Information on this data set, namely the column categories 
df.info()


# ### B) Data Statistics (includes beg. and end of data)

# In[9]:


df.describe()


# In[10]:


df.head ()


# In[11]:


df.tail()


# In[12]:


#This shows the spending categories we are referring to in this analysis 

def user_defined_function(Goods):
    for x in Goods:
         print(x)
Goods = ["Books","Clothing","Electronics"]
user_defined_function(Goods)


# ### C) Box Plot on Product Price, Age, Quantity, Purchase Amount

# In[91]:


plt.figure(1, figsize=(12, 8))

for i in range(0, 4):  
    print(i)
    plt.subplot(2, 2, i+1)  
    plt.boxplot(df[df.columns[i]])
    plt.title(df.columns[i])

plt.show()


# #### Analysis: 
# 
# From this data set we can see that on average, consumers around the age of 40 tend to shop more in e commerce sites. Those consumers who shop at eCommerce, for example Amazon, tend to spend relatively more with an overall average purchase amount being 3k. 

# ### D) Describe a Typical Customer & Purchase Items and Cost

# In[98]:


x= "Mary is 49 years old."
y=" She bought 1 item"
z= " for $449."

print(x+y+z)


# In[16]:


user_defined_function = 'f'

def f(qty, item, price):
    print(f'{qty},{item} cost ${price:.2f}')
    
f(3, ' electronics', 740)

