import time
import random


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def stack_func():
    print('\nstack function starting!')
    stack = Stack()
    print('stack.is_empty = ', stack.is_empty())
    stack.push(1)
    print('stack.is_empty = ', stack.is_empty())
    item = stack.pop()
    print('pop item = ', item)
    print('stack.is_empty = ', stack.is_empty())

    for i in range(0, 6):
        stack.push(i)
    print(stack.peek())
    print(stack.size())


def reverse_func():
    print('\nreverse function starting!')
    stack = Stack()
    for c in "Hello":
        stack.push(c)
    reverse = ''
    while stack.size():
        reverse += stack.pop()
    print('reverse strings = ', reverse)


def queue_func():
    print('\nqueue function starting!')
    a_queue = Queue()
    print(a_queue.is_empty())

    for i in range(5):
        a_queue.enqueue(i)
    print(a_queue.size())

    while a_queue.size():
        print('pop item = ', a_queue.dequeue())
    print()
    print('a_queue size = ', a_queue.size())


def simulation_line(till_show, max_time):
    """
    映画の行列のシミュレーション
    :param till_show: 映画が始まるまでの時間
    :param max_time: 一人当たりのチケット購入時間
    :return:
    """
    print('ticket simulation starting!')
    pq = Queue()
    tix_sold = []

    for i in range(100):
        pq.enqueue('person' + str(i))

    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
    return tix_sold


if __name__ == '__main__':
    stack_func()
    reverse_func()
    queue_func()
    print(simulation_line(5, 1))
