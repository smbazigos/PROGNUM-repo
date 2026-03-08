#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

A=float(input("Input A: "))
x0=float(input("Input x0: "))
sigma=float(input("Input sigma: "))
z0=float(input("Input z0: "))
    
low=float(input("Input the lower limit: "))
high=float(input("Input the higher limit: "))

def gauss_int(x):
    return gauss(x, A, x0, sigma, z0)
Area = quad(gauss_int, low, high)[0]

ini=x0 - 5*sigma
final= x0 + 5*sigma

x=np.linspace(ini, final, 500)
y=gauss(x, A, x0, sigma, z0)

plt.figure(figsize=(8,5))
xfill = np.linspace(low,high,100)
plt.fill_between(xfill,gauss(xfill,A,x0,sigma,z0), color='red', alpha=0.5, label=f'Area={area}')
plt.plot(x,y,label='Gaussian', color='black')
plt.title("Gaussian Graph")
plt.legend()
plt.grid(True)
plt.show()

