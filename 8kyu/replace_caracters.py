"""
Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.
"""

input_str = "111111115555555%%%%%%%%000000000"


def correct(string):
    string = string.replace("1", "I").replace("0", "O").replace("5", "S")
    print(string)
    return string


correct(input_str)
