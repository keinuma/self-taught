class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        name = self.__class__
        print('I am a shape {}'.format(name))


class Rectangle(Shape):
    def __init__(self, w, l):
        super().__init__()
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len) * 2


class Square(Shape):
    def __init__(self, l):
        super().__init__()
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, l):
        self.len += l


def challenge1():
    rec1 = Rectangle(12, 4)
    sq1 = Square(6)
    print('Rectangle perimeter = {}'.format(rec1.calculate_perimeter()))
    print('Square perimeter = {}'.format(sq1.calculate_perimeter()))


def challenge2():
    sq2 = Square(12)
    print(sq2.calculate_perimeter())
    sq2.change_size(-1)
    print(sq2.calculate_perimeter())


def challenge3():
    rec2 = Rectangle(7, 9)
    sq3 = Square(66)
    rec2.what_am_i()
    sq3.what_am_i()


class Horse:
    def __init__(self, name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider


class Rider:
    def __init__(self, name):
        self.name = name


def challenge4():
    toyo = Rider('Toyota')
    north_black = Horse('North Black', 'black', toyo)
    print(north_black.rider.name)


if __name__ == '__main__':
    challenge1()
    challenge2()
    challenge3()
    challenge4()
