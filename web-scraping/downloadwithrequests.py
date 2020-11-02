#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:44:27 2020

@author: Aps
"""

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

"""
The iter_content() method returns “chunks” of the content on each
iteration through the loop. Each chunk is of the bytes data type, and you
get to specify how many bytes each chunk will contain.
"""