#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xml.dom.minidom

doc = xml.dom.minidom.parse("filename.xml")

# searcg for the first tag name
print(doc.nodeName)
print(doc.firstChild.tagName)

# list the content of tag
skills = doc.getElementsByTagName("skill")
for skill in skills:
    print(skill.getAttributes("name"))

# create a new XML tag into the doc
newSkill = doc.createElement("skill")
newSkill.setAttribute("name", "jQuery")
doc.firstChild.appendChild(newSkill)

