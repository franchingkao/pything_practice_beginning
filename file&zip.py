#!/usr/bin/env python
# coding: utf-8

# In[29]:


myFile = open("file.txt", "w")


# In[30]:


for i in range(1,10):
    myFile.write(f"the {i} line\n")


# In[75]:


myFile.close()


# myFile = open("file.txt", "r")

# In[76]:


myFile = open("file.txt", "r")


# In[37]:


print("Reading....\n"+myFile.read())


# In[93]:


for line in myFile:
    h = line.replace("the", "replace")
    print(h)


# In[51]:


myFile.readline()


# In[78]:


myFile = open("file2.txt", "w")


# In[79]:


myFile.write("whatever")


# In[80]:


myFile.close()


# In[81]:


import zipfile


# In[84]:


zip = zipfile.ZipFile('Practice/file.zip','r')


# In[85]:


print(zip.namelist())


# In[86]:


for meta in zip.infolist():
    print(meta)


# In[90]:


info = zip.getinfo("file1.txt")
print(info)


# In[91]:


print(zip.read("file1.txt"))


# In[92]:


with zip.open("file1.txt") as f:
    print(f.read())


# In[97]:


#zip.extract("filename.txt")
zip.extractall()

