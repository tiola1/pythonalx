
class Vector:

    def __ init__(self, x, y):
    self.x = x
    self.y = y

    def __add__(self, other):
        return Vector (self.x + other.x, self.y +other.y)

    def __sub__(self, other):
        if instance (other, int):
        return Vector (self.x - other.x, self.y - other.y)

    def __mul__(self,other):
        return self.x*other.y + self.y*other.x

