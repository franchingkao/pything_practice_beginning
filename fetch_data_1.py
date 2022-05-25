#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request


# In[7]:


weburl = urllib.request.urlopen("http://www.google.com")
print("request code: ", weburl.getcode())

data = weburl.read()
print(data)

