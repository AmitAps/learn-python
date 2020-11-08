Everything is an object.

def is used to define a function, class is used to define a class.

What is a class?
--> Simply a logical grouping of data and functions(The latter of which are frequently referred to as "methods" when defied without a class).


**Instance Attributes and Methods***
An function defined in a class is called a "method". Methods have access to all the data contained on the instance of the object;
they can access and modify anything previously set on self.
Because they use self, they require an instance of the class in order to be used. For this reason, they're often referred to as "instance methods".


***Static Methods***
Class attributes are attributes that are set at the class-level, as opposed to the instance-level.
Normal attributes are introduced in the __init__ method, but some attributes of a class hold for all instances in all cases.



A Car always has four wheels, regardless of the make or model.
 Instance methods can access these attributes in the same way they access regular attributes: through self (i.e. self.wheels).

There is a class of methods, though, called static methods, that don't have access to self. Just like class attributes,
they are methods that work without requiring an instance to be present. Since instances are always referenced through self,
static methods have no self parameter.


Inheritance
While Object-oriented Programming is useful as a modeling tool, it truly gains power when the concept of inheritance is introduced.
Inherticance is the process by which a "child" class derives the data and behavior of a "parent" class.


Class Methods
A variant of the static method is the class method. Instead of receiving the instance as the first parameter, it is passed the class. It, too, is defined using a decorator:
