# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:51:04 2020

@author: Administrator
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 


t=np.arange(0,1,0.001)
ft=5*np.sin(2*np.pi*50*t)

fig=plt.figure(figsize=(10,6))
for k in range(1,9):
    fig.add_subplot(2,4,k)
    plt.plot(t,k*ft)
        
