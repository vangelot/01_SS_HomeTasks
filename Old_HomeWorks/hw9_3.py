class Paralelogram:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_area(self):
        return self._width*self._length

class Square(Paralelogram):
    def get_area(self):
        if self._width == self._length:
            return self._width*self._length
        else:
            return "incorrect object"

a = Paralelogram(2, 6)
print(a.get_area())

b = Square(2, 6)
c = Square(4, 4)

print(b.get_area())
print(c.get_area())