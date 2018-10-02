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