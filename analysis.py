#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


data=pd.read_csv(r"C:\Users\91703\Downloads\Modified_global.csv")
df=pd.DataFrame(data)
print("DATA IS IMPORTED")
df.head()


# In[7]:


df.info()


# In[8]:


df.shape


# In[9]:


df.columns


# In[17]:


df=df[["iyear", "imonth","iday","country_txt","region_txt","eventid","attacktype1_txt","target1","nkill","nwound"]]
df.head()


# In[19]:


df.rename (columns={"iyear":"Year","imonth":"Month","iday":"Day","country_txt":"Country", "region_txt":"Region","attacktype1_txt":"Attack Type","nkill":"Killed","nwound":"Nwound"},inplace=True)


# In[20]:


df.head()


# In[21]:


df.info()


# In[22]:


df.isnull().sum()


# In[24]:


df["Nwound"]=df["Nwound"].fillna(0)
df["Nwound"]=df["Nwound"].fillna(0)


# In[25]:


df.describe()


# In[29]:


df.columns


# In[27]:


yk=df[["Year",'Killed']].groupby("Year").sum()
yk.head()


# In[30]:


df.head(30)


# In[ ]:




