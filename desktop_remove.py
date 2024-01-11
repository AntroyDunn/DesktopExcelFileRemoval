# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:41:24 2023

@author: CouryDunn
"""


import os

def srcpath():
    src = "C:/Users/CouryDunn/OneDrive - The Insights Family/Desktop/"
    return src

def remove_desk(src):        
    for x in os.listdir(src):
        print(src + x)
        if x.endswith('.xlsm') or x.endswith('.xlsx'):
         os.remove(src + x)       
         
src = srcpath()
remove_desk(src)
def greeting():
   print("Hi Coury, that's great!")

