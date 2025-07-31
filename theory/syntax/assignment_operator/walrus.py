"""
The walrus operator allows you to assign a value to a variable as part of an expression.
"""

if (value := input("Enter something: ")) == "hello":
    print("You said hello!")


"""
This is used widely in list comprehensions which makes it very valuable.
"""


# let's create some naive logic
my_list: list[int] = []
for x in range(100):
    if x * 2 > 10:
        my_list.append(x * 2)

"""
Note that x * 2 hapenes twise which is kinda dubious. Let's hide it behind y variable.
"""

for x in range(100):
    y = x * 2
    if y > 10:
        my_list.append(y)


"""
Now for each loop iteration y is assigned to x * 2. Better, but hey, its noob code right? 
Let's make it Pythonic masterpiece with comprehensions.
"""


my_beautiful_list = [x * 2 for x in range(100) if x * 2 > 10]


"""
Now we made a comprehension that looks so good, but still this x * 2 spoild the beauty.
How to get rid of it? There is not room any longer to hide it inside y variable. 
This must happen dynamically, remember? For each iteration of for loop there is separate x value.
Now assingent expression comes into play.
"""


my_perfect_list = [y for x in range(100) if (y := x * 2) > 10]
print(my_beautiful_list)

"""
:= in the list comprehension basically means:
For each new x create a variable that is x * 2 to hide this repeterive expression.
This works when we need to create a variable inside the list comprehension where is no room for 
y = x * 2 or something like that. 
"""
