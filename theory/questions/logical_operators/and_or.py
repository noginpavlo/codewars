"""
How 'and' and 'or' logical operators work?

AND Operator:
>>>Evaluates left to right.
>>>Returns the first falsy value, or the last value if all are truthy.
>>>Short-circuits: Stops evaluating as soon as a falsy value is found.

OR Operator:
>>>Evaluates left to right.
>>>Returns the first truthy value, or the last value if all are falsy.
>>>Short-circuits: Stops evaluating as soon as a truthy value is found.
"""

"""
What values are truthy, what are faulsy?

================================================================================
FAULSY
>>>None
>>>False
>>>0 int, 0.0 float, 0j (complex number -- maths)
>>>'' (empty string)
>>>[] (empty list)
>>>{} (empty dict)
>>>() (empty tuple)
>>>set(), frozenset() (empty)
>>>range(0)
>>>Objects with __bool__ or __len__ returning False or 0

================================================================================
TRUTHY
>>>True
>>>Non-zero numbers (e.g., 1, -5, 2.3)
>>>Non-empty strings, lists, dicts, sets, etc.
>>>Custom objects unless explicitly falsy
"""


"""
================================================================================
Now what will this code print?
================================================================================
"""


def func1():
    print(1)


def func2():
    print(2)


result1 = func1() and func2()
result2 = 0 or "5"
print(result1)
print(result2)
