#!/usr/bin/env python
# coding: utf-8

# In[31]:


import calendar
import datetime
from datetime import date


# In[36]:


c = calendar.TextCalendar(calendar.FRIDAY)
str = c.formatmonth(2022, 1, 0, 0)
print(str)


# In[5]:


hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2022, 1)
print(str)


# In[6]:


for i in c.itermonthdays(2022,1):
    print(i)


# In[10]:


for month in calendar.month_name:
    print(month)
for day in calendar.day_name:
    print(day)


# In[34]:


for m in range(1,13):
    cal = calendar.monthcalendar(2022, m)
    
    if cal[0][4] != 0:
        d = date(date.today().year, m, cal[0][4])
        print(d)
    else:
        d = date(date.today().year, m, cal[1][4])
        print(d)
    


# In[38]:


#other solution
# weekone = cal[0]
# weektwo = cal[1]
# #if weekone[calendar.FRIDAY] != 0:
# print(weektwo)    

