class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print('{} by {}'.format(self.width, self.len))


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


class Person:
    def __init__(self):
        self.name = 'Bob'


def class_var():
    r1 = Rectangle(10, 24)
    r2 = Rectangle(20, 40)
    r3 = Rectangle(100, 200)
    print('three times call Rectangle instance {}, {}, {}'.format(r1, r2, r3))
    print(Rectangle.recs)


def special_method():
    lion = Lion('Dillbert')
    print(lion)
    x = AlwaysPositive(-20)
    y = AlwaysPositive(10)
    print(x + y)


def is_entry():
    bob = Person()
    same_bob = bob
    print(bob is same_bob)

    another_bob = Person()
    print(bob is another_bob)


if __name__ == '__main__':
    class_var()
    special_method()
    is_entry()
