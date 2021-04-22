#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:12:06 2021

@author: meghagupta
"""

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

#these 2 lines for making box figure function is for making for box
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.6,0.6])    #values in add_axes is to define height and width  of box

X=np.linspace(0,5,10)  #linspace is used to input values linespace(start value ,end value, number of values from start to end eg we need 10 values in between 0 to 5)
Y = X**2

axes.plot(X,Y,'r')   # plot func for plotting line graph and r defines red line will be drawn like b for blue
axes.set_xlabel('X-axis')
axes.set_ylabel('Y-axis')
axes.set_title('Line Graph')



#for multi line plot
t=np.arange(0.,5.0,0.2)    #it will give values from 0 to 5 with difference of 0.2
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g*')


