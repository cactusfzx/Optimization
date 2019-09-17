# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:42:19 2019

@author: Omkar
"""

import numpy as np

def F(x,y):
    return ((x)**2 + (y)**2)

point_x = np.random.uniform(0,1)
point_y = np.random.uniform(0,1)

Energy = F(point_x,point_y)

x =[]
y =[]

new_Energy = []
for i in np.arange(100):
    h = 0.1*np.random.uniform()
    N_point1 = point_x + h
    N_point2 = point_y + h
    Energy_1 = F(N_point1,N_point2)
    point_x = N_point1
    point_y = N_point2
    x.append(N_point1)
    y.append(N_point2)
    new_Energy.append(Energy_1)
    
min_index = np.argmin(new_Energy)
min_x = x[min_index]
min_y = y[min_index]
 
print("Optimum value of X is ",min_x)
print("Optimum value of Y is ",min_y)