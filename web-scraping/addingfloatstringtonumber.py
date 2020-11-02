#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:34:20 2020

@author: Aps
"""
tmp = ''
num = 0
s = '1.23,2.4,3.123'
#number = float(s)
for ch in s:
    if ch != ',':
        tmp = tmp + ch
    elif ch == ',':
        num = num + float(tmp)
        tmp = ''

# Also include last float number in sum and show result
print('The sum of all numbers is:', num + float(tmp))