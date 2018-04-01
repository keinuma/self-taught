# カプセル化
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len


class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


class PublicPrivateExample:
    def __init__(self):
        self.public = 'safe'
        self._unsafe = 'unsafe'

    def public_method(self):
        # clientが使っても良い
        pass  # pass文は、文必須な構文で省略する際に使用

    def _unsafe_method(self):
        # clientが使うべきではない
        pass


# 継承
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print('{} by {}'.format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print('I am {} by {}'.format(self.width, self.len))


class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


def check_data_class():
    data_one = Data()
    # numsがタプルに変更されるとエラーになる
    data_one.nums[0] = 100
    print(data_one.nums)

    data_two = Data()
    data_two.change_data(0, 100)
    print(data_two.nums)


def check_shape():
    my_shape = Shape(20, 25)
    my_shape.print_size()
    a_square = Square(20, 20)
    print(a_square.area())
    a_square.print_size()


def check_person_dog():
    mick = Person('Mick Jagger')
    stan = Dog('Stanley', 'Bulldog', mick)
    print(stan.owner.name)


if __name__ == '__main__':
    check_data_class()
    check_shape()
    check_person_dog()
