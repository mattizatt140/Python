class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return "Coordinate(" + str(self.x) + ", " + str(self.y) + ")"
    def __sub__(self, other):
        temp = Coordinate(None, None)
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        return temp
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

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
    def convert(self):
        return self.numer / self.denom

class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ', '
        return '{' + result[:-2] + '}'
    def intersect(self, other):
        inter = intSet()
        for i in self.vals:
            if i in other.vals:
                inter.insert(i)
        return inter
    def __len__(self):
        return len(self.vals)

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, age):
        assert type(age) == int, 'set_age arg not int'
        self.age = age
    def set_name(self, name=""):
        assert type(name) == str, 'set_name arg not str'
        self.name = name
    def __str__(self):
        return "animal: " + str(self.name) + ": " + str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")

set = intSet()
for i in range(20):
    set.insert(i)

print(set)