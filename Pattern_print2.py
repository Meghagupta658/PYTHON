#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:04:16 2020

@author: meghagupta
"""

print("Hello world")

for i in range(1,6):
    for j in range(1,i+1):
        print(j*2, end="")
        
    print() 

    
for i in range(6,0,-1):
    
    for j in range(1,i):
        print(j*2, end="")
        
    print()