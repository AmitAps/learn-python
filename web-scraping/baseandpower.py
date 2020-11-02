#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:05:09 2020

@author: Aps
"""
"""
Write a program that asks the user to enter an integer and prints two integers, root
and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no
such pair of integers exists, it should print a message to that effect.
"""
x = int(input("Enter an integer: "))
root = 0
#pwr = 0
while root < abs(x):
    root += 1
    for pwr in range(1,6):
        if root ** pwr == abs(x):
            if x < 0:
                print("Root is",-root, "to the power of", pwr, "=", x)
            else:
                print("Root is", root, "pwr is ", pwr, "=", x)
        
                  
                
        