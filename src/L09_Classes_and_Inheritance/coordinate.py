# An example of a class object, and instances of that class

class Coordinate(object):

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, other) -> float:
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self) -> str:
        return f"<{self.x},{self.y}>"

    def __sub__(self, other) -> object:
        return Coordinate(self.x - other.x, self.y - other.y)


c = Coordinate(3, 4)
origin = Coordinate(0, 0)

# __str__ methods are called by the print() function
print(c)

# Calling the c Coordinate instance's distance method
print(c.distance(origin))

# Another way of expressing this:
print(Coordinate.distance(c, origin))

# Check whether c is an instance of Coordinate, returns a Boolean
print(isinstance(c, Coordinate))

# %%
