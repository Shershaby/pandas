#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv(r'F:\AI Diploma\New Era\S1\allyears.csv')
print(df.head())


# In[2]:


df.loc[0:10,['name','sex']]


# In[3]:


df.iloc[0:10]


# In[4]:


males = df[df.sex == 'M']
males_ = males.head()
males_


# In[5]:


year = df[df.name == 'Mary']
year_ = year.head()
year_


# In[40]:


females = df[df.sex == 'F']
females_ = females.head()
females_
females_.plot(kind = 'hist',edgecolor='black')
plt.show()


# In[35]:


df.median()


# In[8]:


df.max()


# In[9]:


df.min()


# In[10]:


df.std()


# In[11]:


df[['year','name']].head()


# In[12]:


df.set_index(['sex', 'year']).sort_index()


# In[13]:


df.columns


# In[14]:


df[['name','number','sex']]


# In[15]:


df[df.name == 'Mary']


# In[16]:


df.describe()


# In[22]:


df['Total'] = df.iloc[:, 2:4].sum(axis=1)
df.head()


# In[33]:


df[(df.sex == 'F') & (df.year == 1880)].head(50)


# In[ ]:




