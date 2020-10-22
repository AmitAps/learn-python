#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:48:37 2020

@author: Aps
"""

import turtle
def draw_square(animal, size):
    """
    Make animal draw a sqare with sides of length size

    """
    for _ in range(4):
        animal.forward(size)
        animal.left(90)
        
window = turtle.Screen()  
window.bgcolor("cyan")
window.title("Amit meets a fucntion")


alex = turtle.Turtle()
draw_square(alex, 70)
window.mainloop()


