def fizzbuzz(n):
    for i in range(1, n+1):
        three_times = (i % 3 == 0)
        five_times = (i % 5 == 0)
        if three_times and five_times:
            print('FizzBuzz')
        elif three_times:
            print('Fizz')
        elif five_times:
            print('Buzz')
        else:
            print(i)


def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


def palindrome(word):
    word = word.lower()
    return word == word[::-1]


def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)


def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)


def bottles_of_beer(bob):
    """Prints Bottle of Beer on the Wall lyrics

    :param bob: Must be a positive integer
    """
    if bob < 1:
        print("""
        No more bottles of beer on the wall.
        No more bottles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""
    {} bottles of beer on the wall
    {} bottles of beer.
    Take on down, pass it around,
    {} bottles of beer on the wall.
    """.format(tmp, tmp, bob))
    bottles_of_beer(bob)


if __name__ == '__main__':
    print('FizzBuzz time!')
    fizzbuzz(100)
    numbers = range(0, 100)
    print('\nlinear indexing time!')
    s1 = ss(numbers, 2)
    print(s1)
    s2 = ss(numbers, 202)
    print(s2)
    print('\npalindrome time!')
    print(palindrome('Mother'))
    print(palindrome('Mom'))
    print('\nanagram time!')
    print(anagram('cinema', 'iceman'))
    print(anagram('leaf', 'tree'))
    print('\ncount characters time!')
    count_characters('Dynasty')
    print('\nrecursion time!')
    bottles_of_beer(99)
