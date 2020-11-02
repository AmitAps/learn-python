#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:07:45 2020

@author: Aps
"""
#mapIt.py - Launches a map in the browser using an address from the 
#command line or clipboard.

import webbrowser, sys,pyperclip
if len(sys.argv) > 1:
    #Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    #Get address from clipboard.
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)