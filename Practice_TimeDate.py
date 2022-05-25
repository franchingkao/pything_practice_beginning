#!/usr/bin/env python
# coding: utf-8

# In[6]:


import calendar


# In[7]:


def weekday_count(wd, y, m):
    cd = calendar.monthcalendar(y, m)
    count = 0

    for i in cd:
        if i[wd] != 0:
            count += 1
            
    return count


# In[ ]:


run = True
while run:
    try:
        w = int(input("""Which day of the week do you want to count?
                    0: Mon
                    1: Tue
                    2: Wed
                    3: Thur
                    4: Fri
                    5: Sat
                    6: Sun
                    7: exit\n"""))
        if w == 7:
            run = False
            print("Bye.")
            break

        y = int(input("Enter the year: "))
        m = int(input("Enter the month: "))

        result = weekday_count(w, y, m)
        print(f"There are {result} of those days in the month and year specified.")
        print("-----------------------")
    
    except Exception as e:
        print(e)
        print("Sorry it\'s not a valid input. Please try again.")

