class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name):
        """Return a Customer object whose name is *name*."""
        self.name = name

    def set_balance(self, balance=0.0):
        """Set the customer's starting balance."""
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance


"""
This may look like a reasonable alternative; we simply need to call set_balance before we begin using the instance.
There's no way, however, to communicate this to the caller. Even if we document it extensively,
we can't force the caller to call amit.set_balance(1000.0) before calling amit.withdraw(100.0).
Since the amit instance doesn't even have a balance attribute until jeff.set_balance is called,
 this means that the object hasn't been "fully" initialized.

The rule of thumb is, don't introduce a new attribute outside of the __init__ method, otherwise you've given the caller an object that isn't
fully initialized
"""
