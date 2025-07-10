from functools import wraps

"""
Lazy Decorator Function
You have decided to play a prank on your programmer friend.

You want to make his code "Lazy". And not in the good way. You want his
functions to only run normally every nth run, otherwise doing nothing.

To do this, you are going to write a function decorator @lazy(n) where n is the
frequency of 'normal' runs. For example, if n == 4, then after the first
successful run, the next three calls to this function will do nothing, and then
the 5th run'll run normally again. (The first run should always be successful,
except for n == -1 which is always lazy).

However, if n is a negative number, then the frequency is inverted
(ie. @lazy(-4) means that only every 4th run is lazy, the rest are normal.).

If n == 1, then the function should always be normal, and if n == -1 then the
function should always be lazy. n == 0 will never be tested.

Note: When the lazy function 'does nothing', that means it immediately returns
None. No lines of the 'normal' function should be run at all.

Example Code

@lazy(4)
def half(x):
  return x/2

print(half(10)) # 5  <- Remember, First run should be normal
print(half(77)) # None
print(half(63)) # None
print(half(2))  # None
print(half(38)) # 19 <- Every nth run (in this case 4) should also be normal

@lazy(-3)
def output_str(s):
  print(s)

output_str('Foo') # Foo <- Starts normal
output_str('Bar') # Bar
output_str('Pikachu') # Nothing printed <- Every nth run is lazy
output_str('Gla') # Gla
"""


def lazy(n):
    def decorator(func):
        count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1

            if n == 1:
                return func(*args, **kwargs)
            elif n == -1:
                return None
            elif n > 1:
                if (count - 1) % n == 0:
                    return func(*args, **kwargs)
                return None
            elif n < -1:
                if count % abs(n) == 0:
                    return None
                return func(*args, **kwargs)

        return wrapper

    return decorator


@lazy(4)
def half(x: int):
    return x / 2


print(half(10))  # 5  <- Remember, First run should be normal
print(half(77))  # None
print(half(63))  # None
print(half(2))  # None
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # None
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # one
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
print(half(38))  # 19 <- Every nth run (in this case 4) should also be normal
