#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("I am imported!!!")


# In[1]:


test ='Testing module!!!'


# In[ ]:


def find_index(to_search,target):
    for i,value in enumerate(to_search):
        if value==target:
            return i
    
    return -1

