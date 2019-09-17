import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib.pyplot as pl
from collections import Counter

def F(x,y):
    return (1-x)**2 + 100*(y-(x**2))**2

point_x = np.random.uniform(-3,3)
point_y = np.random.uniform(-3,3)

Energy = F(point_x,point_y)
x=[]
y=[]
new_Energy =[]
new_Energy.append(Energy)
x.append(point_x)
y.append(point_y)
len1=[]
len2=[]
for i in range(500):
   
    h1 = np.random.uniform(-0.5,0.5)*0.1
    h2 = np.random.uniform(-0.5,0.5)*0.1
    N_point1 = point_x + h1
    N_point2 = point_y + h2
    Energy_1 = F(N_point1,N_point2)
    delta = Energy_1 - Energy
    
    if delta <= 0 | (np.random.uniform(0,1) < np.exp(-delta)):
        
        point_x = N_point1
        point_y = N_point2    
        x.append(point_x)
        y.append(point_y)
        Energy = Energy_1
        new_Energy.append(Energy)
        #m_1 = Counter(new_Energy)
        len1.append(Energy)
        m1 = len(len1)
    
    else:
        
        point_x = point_x
        point_y = point_y
        x.append(point_x)
        y.append(point_y)
        Energy = Energy
        new_Energy.append(Energy)
        #m2 = Counter(new_Energy)
        len2.append(Energy)
        m2 = len(len2)
        
#m2 = 500 - m1
prob = 0.95
Denom = (prob * (m1 + m2) - m1) / m2
Del_F =  sum(len2) / m2 
T0 = (-Del_F) / np.log(Denom)

Lmat = 5
Zmin = 100
le=[]
for t in range(int(T0)):
        
    for i in range(100):
       
        h = np.random.uniform(-0.5,0.5) * 0.1
        N_point1 = point_x + h
        N_point2 = point_y + h
        Energy_1 = F(N_point1,N_point2)
        delta = Energy_1 - Energy
        
        if (delta <= 0) | (np.random.uniform(0,1) < np.exp(-delta / T0)):
            
            point_x = N_point1
            point_y = N_point2    
            x.append(point_x)
            y.append(point_y)
            Energy = Energy_1
            new_Energy.append(Energy)
            le.append(Energy)
            m = len(le)
            
    if m >= Zmin:
        T0 = T0 * 0.9
print("Optimum value of x is ",point_x)
print("Optimum value of y is ",point_y)
print("Optimum Function Value is ",Energy)            