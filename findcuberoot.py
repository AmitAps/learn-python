#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:26:32 2020

@author: Aps
"""

#find the cube root of a perfect cube

"""
The abs() function of Python's standard library returns the absolute value of the given number. Absolute value of a number is the value without considering its sign. Hence absolute of 10 is 10, -10 is also 10. If the number is a complex number, abs() returns its magnitude.-
"""

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
    #print('Value of the decrementing function abs(x) - ans**3 is', abs(x) - ans**3)
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans 
    print('Cube root of', x, 'is', ans)