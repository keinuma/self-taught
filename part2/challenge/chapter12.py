import math


class Apple:
    def __init__(self, c, w, r, a):
        self.color = c
        self.weight = w
        self.radius = r
        self.area = a


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2


class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def area(self):
        return self.bottom * self.height / 2


class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6


if __name__ == '__main__':
    circle1 = Circle(22)
    print(circle1.area())
    triangle1 = Triangle(21, 8)
    print(triangle1.area())
    hexagon = Hexagon(2, 4, 6, 7, 21, 3)
    print(hexagon.calculate_perimeter())
