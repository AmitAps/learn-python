#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:52:26 2020

@author: Aps
"""



import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

type(res)
Out[4]: requests.models.Response

#check if everything is going okay or not
res.status_code == requests.codes.ok
Out[5]: True

len(res.text)
Out[6]: 178978

print(res.text[:205])
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it awa


#checking for errors
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

res.raise_for_status()
Traceback (most recent call last):

  File "<ipython-input-9-cd6be6b74546>", line 1, in <module>
    res.raise_for_status()

  File "/home/Aps/anaconda3/lib/python3.8/site-packages/requests/models.py", line 941, in raise_for_status
    raise HTTPError(http_error_msg, response=self)

HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist


