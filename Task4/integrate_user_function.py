#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, tan, exp, pi
import scipy.integrate

fun = (input(f"Input a function: "))
a = float(input(f"Input the lower bound a: "))
b = float(eval(input(f"Input the upper bound b: ")))
n = 10000

f = lambda x: eval(fun)
result = scipy.integrate.quad(f, a, b)[0]
print(f"The scipy integration gives: {result}")

x = np.random.uniform(a, b, 10000)
y = eval(fun)
integral = (b-a)/n * np.sum(y)
print(f"MOnte Carlo integration gives: {integral}")

