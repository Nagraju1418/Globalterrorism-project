#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("C:\\Users\\91703\\Downloads\\Modified_global.csv")


# In[5]:


data.info()


# In[6]:


print(data.head())


# In[7]:


data['Year'] = pd.to_datetime(data['iyear'], format='%Y')
yearly_attacks = data['Year'].dt.year.value_counts().sort_index()


# In[8]:


plt.figure(figsize=(12, 6))
yearly_attacks.plot(kind='line', marker='o')
plt.title('Global Terrorism Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.grid(True)
plt.show()


# In[9]:


# Analyze types of attacks
attack_types = data['attacktype1_txt'].value_counts()


# In[10]:


# Plot the most common types of attacks
plt.figure(figsize=(10, 6))
attack_types.plot(kind='bar')
plt.title('Most Common Types of Terrorist Attacks')
plt.xlabel('Attack Type')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=90)
plt.show()


# In[1]:


from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()

# Read data from a source (e.g., CSV file)
df = spark.read.csv(r"C:\Users\91703\Downloads\Modified_global.csv", header=True, inferSchema=True)

# Now you can work with the 'df' DataFrame
df.printSchema()


# In[2]:


df.show()


# In[17]:


df.head(20)


# In[19]:


num_columns = len(df.columns)
print("Number of columns:", num_columns)


# In[ ]:




