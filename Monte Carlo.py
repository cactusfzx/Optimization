# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:02:48 2019

@author: Omkar
"""
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as pl
def F(x,y):
    return (1-x)**2 + 100*(y-(x**2))**2

point_x = np.random.uniform(0,1)
point_y = np.random.uniform(0,1)

Energy = F(point_x,point_y)

x =[]
y =[]

new_Energy = []
new_Energy.append(Energy)
x.append(point_x)
y.append(point_y)
for i in range(0,10000):
    h = np.random.uniform(0,1)
    N_point1 = point_x + h
    N_point2 = point_y + h
    Energy_1 = F(N_point1,N_point2)
    delta = Energy_1 - Energy
    
    if delta <= 0:
        
        point_x = N_point1
        point_y = N_point2    
        x.append(point_x)
        y.append(point_y)
        Energy = Energy_1
        new_Energy.append(Energy)
    else:
        point_x = point_x
        point_y = point_y
        x.append(point_x)
        y.append(point_y)
        Energy = Energy
        new_Energy.append(Energy)
        
pl.figure()
ax = pl.axes(projection = "3d")
ax.plot3D(x,y,new_Energy,"Red")
pl.show()            
print("Optimum value of X is ",point_x)
print("Optimum value of Y is ",point_y)
print("Optimum Function Value is ",Energy)