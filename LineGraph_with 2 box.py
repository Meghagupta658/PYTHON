#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:26:08 2021

@author: meghagupta
"""

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(X,Y,'r')
axes1.set_xlabel('X-axis')
axes1.set_ylabel('Y-axis')
axes1.set_title('Outer Line Graph')
axes2.plot(Y,X,'g')
axes2.set_xlabel('Y-axis')
axes2.set_ylabel('X-axis')
axes2.set_title('Inner Line Graph')

