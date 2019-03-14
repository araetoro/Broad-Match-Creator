
# coding: utf-8

# In[69]:


import numpy as np
import pandas as pd

key = pd.read_csv('flood_keywords.csv')

keywords = key.iloc[:, -1].values

splitlist = []
new_list = []

for word in keywords:
    splitword = word.split()
    plus = [" +" + word for word in splitword]
    newkey = [''.join(plus[:])]
    newkey.insert(0,"+company")
    new_list.append(newkey)
    
print(new_list)


# In[74]:


for word in keywords:
    splitword = word.split()
    plus = [" +" + word for word in splitword]
    newkey = [''.join(plus[:])]
    newkey.insert(0,"+services")
    new_list.append(newkey)
    
print(new_list)


# In[75]:


for word in keywords:
    splitword = word.split()
    plus = [" +" + word for word in splitword]
    newkey = [''.join(plus[:])]
    newkey.insert(0,"+local")
    new_list.append(newkey)
    
print(new_list)


# In[76]:


for word in keywords:
    splitword = word.split()
    plus = [" +" + word for word in splitword]
    newkey = [''.join(plus[:])]
    newkey.insert(0,"+expert")
    new_list.append(newkey)
    
print(new_list)


# In[ ]:


for word in keywords:
    splitword = word.split()
    plus = [" +" + word for word in splitword]
    newkey = [''.join(plus[:])]
    newkey.insert(0,"+services")
    new_list.append(newkey)
    
print(new_list)


# In[ ]:


for word in keywords:
    splitword = word.split()
    plus = [" +" + word for word in splitword]
    newkey = [''.join(plus[:])]
    newkey.insert(0,"+services")
    new_list.append(newkey)
    
print(new_list)


# In[77]:


np.savetxt("keywords_with_attributes.csv", new_list, fmt="%s")

