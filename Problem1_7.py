# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:57:43 2020

@author: Juan Daniel Velez
"""
#%%
def problem1_7():
    bases = float(input("Enter the length of one of the bases: "))
    base = float(input("Enter the length of the other base: "))
    height = float(input("Enter the height: "))
    averageBases = (bases+base)/2
    area = averageBases*height
    print("The area of a trapezoid with bases",bases,"and",base,"and height",height,"is",area)
