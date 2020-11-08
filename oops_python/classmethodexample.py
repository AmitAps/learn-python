class Vehicle(object):
    """
    A variant of the static method is the class method.
    Instead of receiving the instance as the first parameter, it is passed the class. It, too, is defined using a decorator:
    """
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2
