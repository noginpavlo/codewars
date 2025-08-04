"""
Simply put, don't use mutable objects as the default arguments of functions.
"""

"""
Have a look at this function (that is wrong):
"""


def wrong_user_display(user_data: dict = {"name": "Pablo", "age": 29}):
    name = user_data.pop("name")  # .pop returns value based on key and removes key-value from dict
    age = user_data.pop("age")
    return f"{name}, {age}"


"""
In wrong_user_display function the problem is that the default dict is created onse
when the function is DEFINED not each time when it is called.
So any changes to the 'default value' in the future result in permanent change of this value.
Defalult values of kwargs are stored in __defaults__ attribute inside function objects.
And the as soon as __defaults__[0] let's say is changed in function's body it is permanent
for other function calls that do not specify the kwargs. Default value changes all the time.
"""


"""
Let's have a look at different example with list as a default argument:
"""


def wrong_list_function(def_list: list[int] = []):
    return def_list.append(1)


"""
Here the list will grow in memory each time the function is called, because the list
is stored in __defaults__ attribute and will change each time the .append() method is called
This way for each function call the default value will become [1] then [1, 1] then [1,1,1] etc.
"""


"""
The solution pattern:
Always use None as default and then use or operator like in the following example:
"""


def user_display(user_data=None):
    user_data = user_data or {"name": "Pablo", "age": 29}
    name = user_data.pop("name")  # .pop returns value based on key and removes key-value from dict
    age = user_data.pop("age")
    return f"{name}, {age}"


"""
or operator returns the first truthy value or the last faulsy (if all are falsy).
So if the user_data is not provided as a keyword arg (default falue is None, falsy)
or operator returns first truthy vluee which is {"name": "Pablo", "age": 29}
"""
