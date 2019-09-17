# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:18:19 2019

ACO - clustering_generalized

@author: Omkar
"""

import numpy as np
import pandas as pd 
import warnings
from sklearn.datasets import load_iris
warnings.filterwarnings("ignore")
import random as ran


clust_no = int(input("Enter number of clusters :"))
max_itr = int(input("Enter max_iterations :"))
q0 = float(input("Enter probability q0 :"))
ant_no = int(input("Enter number of Ants :"))

data = load_iris().data
data = pd.DataFrame(data)

for N in range(ant_no):
 
    D=[] ; CLUSTER=[]
    for U in range(max_itr):
                    
        R=[]
        for i in range(len(data)):
            r = [ran.random() for i in range(1,clust_no+1)]
            s = sum(r)
            r = [ i/s for i in r ]
            R.append(r)
        
        pherom_mat = np.matrix(R)
        cluster_1 = []; cluster_2 = [];cluster_3 = []
        CLUST =[]
        CLUST.append(cluster_1);CLUST.append(cluster_2); CLUST.append(cluster_3)
        
        def exploitation(x):
            ind1 = np.argmax(x)
            return (ind1)
        
        def exploration(probability):
              ind2 = np.argmax(probability)
              return(ind2)
          
        IND1=[]; IND2=[]
        for i in range(len(data)):
            q = np.random.uniform(0,1)
            prob = pherom_mat[i][:clust_no] / np.sum(pherom_mat[0])
            if q < q0:
                ind_1 = exploitation(pherom_mat[i])
                IND1.append(ind_1)
                CLUST[ind_1].append(data.iloc[i,:])
            
            else:
                ind_2 = exploration(prob)
                CLUST[ind_2].append(data.iloc[i,:])
        
        cluster_1,cluster_2,cluster_3 = pd.DataFrame(cluster_1),pd.DataFrame(cluster_2),pd.DataFrame(cluster_3)
        cg_1=[]; cg_2=[]; cg_3=[]; cg_4=[]     
        
        CG1 = np.mean(cluster_1); CG2 = np.mean(cluster_2); CG3 = np.mean(cluster_3)
        
        def distance(x,y):
            return np.sqrt(sum(x-y)**2)
        
        dd1 = []
        for i in range(len(CG1)):
            dist1=[]
            for j in range(len(cluster_1)):
                d1 = distance(CG1[i],cluster_1.iloc[j,:])
                dist1.append(d1)
        clust_dist_1 = np.sum(dist1) 
                
        for i in range(len(CG2)):
            dist2=[]
            for j in range(len(cluster_2)):
                d2 = distance(CG2[i],cluster_2.iloc[j,:])
                dist2.append(d2)
        clust_dist_2 = np.sum(dist2) 
        
        for i in range(len(CG3)):
            dist3=[]
            for j in range(len(cluster_3)):
                d3 = distance(CG3[i],cluster_3.iloc[j,:])
                dist3.append(d3)
        clust_dist_3 = np.sum(dist3)        
                
        sum_clust_dist = clust_dist_1 + clust_dist_2 + clust_dist_3
        D.append(sum_clust_dist)
        CLUSTER.append(CLUST)
        min_indx = np.argmin(D)
        bst_clust = CLUSTER[min_indx]
        
    pherom_mat = pd.DataFrame(pherom_mat)
    cls1,cls2,cls3 = list(pd.DataFrame(bst_clust[0]).index),list(pd.DataFrame(bst_clust[1]).index),list(pd.DataFrame(bst_clust[2]).index)
    CLS=[]
    CLS.append(cls1); CLS.append(cls2); CLS.append(cls3); 
    
    for i in range(clust_no):    
        pherom_mat.iloc[CLS[i],0] = pherom_mat.iloc[CLS[i],0] * 1.1
        pherom_mat.iloc[CLS[i],1] = pherom_mat.iloc[CLS[i],1] * 0.9
        pherom_mat.iloc[CLS[i],2] = pherom_mat.iloc[CLS[i],2] * 0.9

Clusters = [cluster_1,cluster_2,cluster_3]
print("Clusters are :",len(cluster_1),len(cluster_2),len(cluster_3))