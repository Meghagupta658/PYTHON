#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:41:08 2021

@author: meghagupta
"""

#1.print 1 to 10 numbers
i=1
while i<=10:
    print(i)
    i=i+1
    
#2.Using break in while loop
i=0
while i<6 :
    i+=1
    if i==3 :
        break
    print(i)
    
#2.Using continue in while loop
i=0
while i<6 :
    i+=1
    if i==3 :
        continue
    print(i)
    
#2.Using else in while loop
i=0
while i<6 :
    print(i)  
    i+=1
else :
    print ("i not less than 6")
    
    
    
    
    
    
         