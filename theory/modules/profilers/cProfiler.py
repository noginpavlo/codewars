import cProfile


def slow_function():
    total = 0
    for i in range(1, 100000):
        total += i**2
    return total


def fast_function():
    return sum(i**2 for i in range(1, 100000))


cProfile.run("slow_function()")
cProfile.run("fast_function()")
