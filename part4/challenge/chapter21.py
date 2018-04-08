class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def reverse(iterable):
    stack = Stack()
    for w in iterable:
        stack.push(w)
    if isinstance(iterable, str):
        r = ''
        while stack.size():
            r += stack.pop()
    elif isinstance(iterable, list):
        r = []
        while stack.size():
            r.append(stack.pop())
    else:
        raise TypeError
    return r


if __name__ == '__main__':
    string = 'yesterday'
    r_string = reverse(string)
    print(r_string)
    numbers = [1, 2, 3, 4, 5]
    r_numbers = reverse(numbers)
    print(r_numbers)
