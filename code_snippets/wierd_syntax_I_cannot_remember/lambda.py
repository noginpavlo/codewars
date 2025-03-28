square = lambda x: x * x
result1 = square(2)
print(f"Result 1: {result1}")

add = lambda a, b: a + b
result2 = add(5, 5)
print(f"Result 2: {result2}")

my_list = [1,2,3,4,5]
squared_list = map(lambda x: x ** 2, my_list)
print(f"My list: {my_list};\nSquared list: {list(squared_list)}")