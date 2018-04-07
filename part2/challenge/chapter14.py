class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        name = self.__class__
        print('I am a shape {}'.format(name))


class Square(Shape):
    square_list = []

    def __init__(self, l):
        super().__init__()
        self.len = l
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, l):
        self.len += l

    def __repr__(self):
        return '{n} by {n} by {n} by {n}'.format_map({'n': self.len})

    def is_same(self, other):
        if self is other:
            return True
        else:
            return False


def challenge():
    sq1 = Square(12)
    sq2 = Square(26)
    sq3 = Square(86)
    print(sq1, sq2, sq3)
    print(Square.square_list)
    same = sq1
    print(sq1.is_same(same))
    print(sq1.is_same(sq2))


if __name__ == '__main__':
    challenge()
