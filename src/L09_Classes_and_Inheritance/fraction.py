class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
            + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)

    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
            - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)

    def convert(self):
        return self.getNumer() / self.getDenom()


oneHalf = fraction(1, 2)
twoThirds = fraction(2, 3)

print(oneHalf.getNumer())
print(fraction.getDenom(twoThirds))

# The built-in __add__ method has been redefined in the fraction class
new = oneHalf + twoThirds
print(new)

threeQuarters = fraction(3, 4)
# The built-in __sub__ method has been redefined in the fraction class
secondNew = twoThirds - threeQuarters
print(secondNew)

print(secondNew.convert())
