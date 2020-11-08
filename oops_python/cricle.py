import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_parameter(self):
        return 2 * math.pi * self.radius

"""
The __init__() is special method known as initializer or constructor. It is invoked everytime after a new object is created in the memory.
The purpose of the initializer method is to create object's attribute with some initial value.
"""
