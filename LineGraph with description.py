#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:10:03 2021

@author: meghagupta
"""

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

fig,ax=plt.subplots()          #subplots func is used to draw multiple graphs
ax.plot(X,X**2,label='Y=X**2')
ax.plot(X,X**3,label='Y=X**3')
ax.legend(loc=2)                #legend function is for adding description in graph
axes.set_xlabel('X-axis')
axes.set_ylabel('Y-axis')
axes.set_title('Line Graph')
