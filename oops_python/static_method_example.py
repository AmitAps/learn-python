class  Car(object):
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
    @staticmethod
    def make_car_sound():
        """
        To make it clear that this method should not receive the instance as the first parameter (i.e. self on "normal" methods),
        the @staticmethod decorator is used
        """
        print('Vrooooommmm!')

"""
 mustang = Car('Ford', 'Mustang')
>>> print(mustang.wheels)
4
>>> print(Car.wheels)
4

"""
"""
A Car always has four wheels, regardless of the make or model. Instance methods can access these attributes in the same way they access
regular attributes: through self (i.e. self.wheels).

There is a class of methods, though, called static methods, that don't have access to self. Just like class attributes,
they are methods that work without requiring an instance to be present.
Since instances are always referenced through self, static methods have no self parameter.
"""
