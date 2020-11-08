"""
Classes can be thought of as blueprints for creating objects. When I define a Customer class using the class keyword, I haven't actually
created a Customer Insted, what I've created is a sort of insturction manual for constructing "Customer" objects.
"""

class Customer(object):
    """
    A Customer of ABC Bank with a checking account. Customers have the following properties:

    Attributes:
        name: A string representating the Customer's name.
        balance: A float tracking the current balance of the Customer's account.
    """
    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""

        self.name = name
        self.balance = balance


    def withdraw(self, amount):
            """
            Return the balance remaining after withdrawin *amount*.
            """
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """
        Return the balance remaining after depositing amount.
        """
        self.balance += amount
        return self.balance

"""
The class Customer(object) line does not create a new customer. That is, just because we've defined a Customer doesn't mean we've created one; we've merely outlined the blueprint to create a Customer object.
To do so, we call the class's __init__ method with the proper number of arguments (minus self, which we'll get to in a moment).
"""

#amit = Customer('amit singh', 1000.0)
"""
 This line simply says "use the Customer blueprint to create me a new object, which I'll refer to as amit."

 The amit object, known as an instance, is the realized version of the Customer class. Before we called Customer(), no Customer object existed. We can, of course, create as many Customer objects as we'd like. 
 There is still, however, only one Customer class, regardless of how many instances of the class we create.
"""
