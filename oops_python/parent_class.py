#INHERITANCE PARENT CLASS
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal :" + str(self.name) + ":" + str(self.age)

class Cat(Animal):
    """
    Inherits all attributes of Animal: __init__(), age, name, get_age(), get_name(),set_age(),set_name(),__str__()
    """
    #Add new functionality with speak() speak method
    def speak(self):
        print("meow")
    #overrides __str__
    def __str__(self):
        return "Cat :" + str(self.name) + ":" + str(self.age)


#PARENT class is Animal
class Person(Animal):
    def __init__(self, name, age):
        #call Animal constructor
        Animal.__init__(self, age)
        #call Animal's method
        self.set_name(name)
        #Add a new attribute
        self.friends = []

    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.appened(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "Year differences")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)



# print("\n------person tests ----")
# p1 = Person("Amit", 30)
# p2 = Person("Aditya", 28)
# print(p1.get_name())
# print(p1.get_age())
# print(p2.get_name())
# print(p2.get_age())
# print(p1)
# p1.speak()
# p1.age_diff(p2)




import random
#Inherits Person and Animal attributes
class Student(Person):
    def __init__(self, name, age, major=None):
        #ASKED Animal CLASS __INIT__ TO INITIALISE NAME AND AGE FOR ME AS YOU KNOW HOW TO
        Person.__init__(self, name, age)
        #ADDS NEW DATA
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching tv")
    #overrides __str__ method
    def __str__(self):
        return "Student :" + str(self.name) + ":" + str(self.age) + ":"+ str(self.major)


print("\n---- Student tests----")
s1 = Student('Amit', 20, 'CS')
s2 =  Student('Nehu', 18)
print(s1)
print(s2)
print(s1.get_name(), "says:", end=" ")
s1.speak()
print(s2.get_name(), "says:", end=" ")
s2.speak()
