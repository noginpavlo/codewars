"""
The walrus operator allows you to assign a value to a variable as part of an expression.

"""


if (value := input("Enter something: ")) == "hello":
    print("You said hello!")


