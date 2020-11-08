class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return(x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "<" + str(self.x)+","+str(self.y)+">"


#conventional way
c = Coordinate(3,4)
zero = Coordinate(0,0)
print(c,zero)
print(c.distance(zero))
print(type(c))
#use isinstance() to check if an object is a Coordinate
print(isinstance(c, Coordinate))

#equivalent to
# c = Coordinate(3,4)
# zero = Coordinate(0,0)
# print(Coordinate.distance(c,zero))
