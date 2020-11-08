"""
A Vehicle is not a real-world object. Rather, it is a concept that some real-world objects (like cars, trucks, and motorcycles) embody.
We would like to use the fact that each of these objects can be considered a vehicle to remove repeated code. We can do that by creating a Vehicle class:
"""

class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    base_sale_price = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Vehicle object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on


    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)


"""
Now we can make the Car and Truck class inherit from the Vehicle class by replacing object in the line class Car(object).
The class in parenthesis is the class that is inherited from (object essentially means "no inheritance". We'll discuss exactly why we write that
 in a bit).
"""
class Car(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Car object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 8000


class Truck(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 10000


A Vehicle is just a concept, not a real thing, so what does it mean to say the following:

v = Vehicle(4, 0, 'Honda', 'Accord', 2014, None)
print v.purchase_price()
A Vehicle doesn't have a base_sale_price, only the individual child classes like Car and Truck do.
The issue is that Vehicle should really be an Abstract Base Class. Abstract Base Classes are classes that are only meant to be inherited from;
you can't create instance of an ABC. That means that, if Vehicle is an ABC, the following is illegal:


v = Vehicle(4, 0, 'Honda', 'Accord', 2014, None)



It makes sense to disallow this, as we never meant for vehicles to be used directly. We just wanted to use it to abstract away some common data
and behavior. So how do we make a class an ABC? Simple! The abc module contains a metaclass called ABCMeta (metaclasses are a bit outside the scope
of this article). Setting a class's metaclass to ABCMeta and making one of its methods virtual makes it an ABC. A virtual method is one that the ABC
 says must exist in child classes, but doesn't necessarily actually implement. For example, the Vehicle class may be defined as follows:

 from abc import ABCMeta, abstractmethod

class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type():
        """"Return a string representing the type of vehicle this is."""
        pass
