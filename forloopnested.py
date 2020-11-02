#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:12:17 2020

@author: Aps
"""
"""
the range function in the outer loop is evaluated only once, but the range function in the
inner loop is evaluated each time the inner for statement is reached.
"""
x = 4
for j in range(x):
    for i in range(x):
        print(i)
        x = 2