#!/usr/bin/env python
# coding: utf-8

# In[1]:


people = {
    'first': ['amit','vinay','ankit'],
    'last':['pratap', 'singh','mishra'],
    'email':['amitoct9@gmail.com','vinaysingh@gmail.com','mishraankit@mai.com']
    
}


# In[2]:


people['email']


# In[3]:


import pandas as pd


# In[4]:


df = pd.DataFrame(people)


# In[5]:


df


# In[6]:


pd['email']


# In[7]:


df['email']


# In[8]:


type(df['email'])


# In[9]:


df.email


# In[13]:


df[['last','email']]


# In[14]:


df[['first','email']]


# In[15]:


df.columns


# In[16]:


df.iloc[0]


# In[17]:


df.iloc[[0,1]]


# In[18]:


df.iloc[[0,1], 2]


# In[19]:


df


# In[20]:


df.loc[0]


# In[21]:


df.loc[[0,1]]


# In[22]:


df.loc[[0,1], 'email']


# In[23]:


df.loc[[0,1],['email','last']]


# In[ ]:




