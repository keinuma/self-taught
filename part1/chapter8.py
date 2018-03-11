import statistics


def challenge1():
    std = statistics.stdev([1., 5., 13., 123.])
    print(std)


def cubed(num: float) -> float:
    return num * num * num
