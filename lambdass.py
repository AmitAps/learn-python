#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:30:31 2020

@author: Aps
"""

f1 = lambda x: x
f1(5)


f2 = lambda x,y: x+y

f2(5,6)

f3 = lambda x,y: 'factor' if(x%y == 0) else 'not factor'

f3(4,6)
