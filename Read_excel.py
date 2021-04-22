#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:18:42 2021

@author: meghagupta
"""

import pandas as pd
dataset = pd.read_excel("3. Descriptive Statistics.xlsx", sheet_name = 0)

dataset.columns

dataset.head()

dataset.info()