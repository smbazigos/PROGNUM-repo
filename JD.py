#!/usr/bin/env python
# coding: utf-8

# In[2]:


def julian_date(day, month, year):
    D=float(day)
    M=int(month)
    Y=int(year)
    
    JD = (367*Y -(7*(Y+(M+9)//12))//4 - (3*(((Y+(M-9)//7)//100) + 1))//4 
          + (275*M)//9 + D + 1721029-0.5)
    return JD

day = float(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

jd = julian_date(day, month, year)
print(f"The Julian Date is: {jd} ")


# In[ ]:




