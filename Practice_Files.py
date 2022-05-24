#!/usr/bin/env python
# coding: utf-8

# In[70]:


import os
#from os import path

totalbytes = 0


# In[71]:


file_list = os.listdir()
for entry in file_list:
    if os.path.isfile(entry):
        databyte += os.path.getsize(entry)


# In[72]:


try:
    os.mkdir("results")
except:
    print("FileExistsError")


# In[73]:


result_file = open("results/myfile.txt", "w+")
if result_file.mode == "w+":
    result_file.write(f"Total bytecount is {databyte}\n")
    result_file.write("File list: \n")
    result_file.write("-----------\n")

    for entry in file_list:
        if os.path.isfile(entry):
            result_file.write(f"{entry}\n")
        
    result_file.close()

