#!/usr/bin/env python
# coding: utf-8

# In[8]:


import urllib.request
import json
# https://docs.python.org/3/library/json.html


# In[42]:


def printResults(data):
    theJSON = json.loads(data)
    
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    
    count = theJSON["metadata"]["count"]
    print(f"{count} events recorded")
    print("--------\n")

    
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("--------\n")
        
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print(i["properties"]["place"])
    print("--------\n")
    
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        placeReports = i["properties"]["place"]
        if feltReports != None and feltReports > 0:
            print(f"in {placeReports}, {feltReports} times")
    print("--------\n")


# In[43]:



urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

webUrl = urllib.request.urlopen(urlData)
print(f"result code: {webUrl.getcode()}")
if webUrl.getcode() == 200:
    data = webUrl.read()
    printResults(data)
else:
    print("error!")

