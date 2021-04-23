#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:17:13 2021

@author: meghagupta
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Data
n=5 
menmean = (20,35,20,35,27)
menstd = (2,3,4,1,2)
womenmean = (25,30,32,33,28)
womenstd = (3,2,5,4,1)

ind=mp.arange(5)
width = 0.25

fig,ax = plt.subplots()
r1=ax.bar(ind, menmean,width,color='r',yerr=menstd)
r2=ax.bar(ind + width, womenmean,width,color='y',yerr=womenstd)


