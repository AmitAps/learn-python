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


# In[ ]:




