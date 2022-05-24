#!/usr/bin/env python
# coding: utf-8

# In[10]:


from datetime import datetime
from datetime import date
from datetime import time

def main():
    today = datetime.today()
    
    #Date components 
    today.day
    today.month
    today.year
    
    #using index to find out the name of weekday
    today.weekday()
    weekdays = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
    weekdays[today.weekday()]
    
    #time
    now = datetime.now()
    time = datetime.time(now) #just time

if __name__ == "__main__": main()


# In[16]:


# date formatting
print(now.strftime("%a, %d, %B, %y"))
# year %y %Y 
# weekday %a %A 
# month %b %B
# day of month %d

# locale's date and time %c
# locale's date %x
# locale's time %X


# In[17]:


# time formatting
print(now.strftime("%I, %H, %M, %S, %p"))
# 12/24 hour %I %H
# minute %M
# second %S
# locale's AM/PM %p


# In[18]:


# make calculation on time
from datetime import timedelta

now = datetime.now()

print(timedelta(weeks = 1, days=365, hours=5, minutes=1))
print("in two weeks and 3 days will be: ", str(now+timedelta(weeks=2, days=3)))


# In[40]:


#countdown
today = date.today()
festival = date(today.year, 6, 3)

if festival < today:
    festival = festival.replace(year = today.year + 1)
    
gap = festival - today
print(f"It\'s {gap.days} days left till Dragon Boat Festival comes.")
#print(festival)
#print(today)

