check_variable = True

def is_valid(f):
    def wrapper():
        if check_variable:
            f()
        else:
            print("for now the world is not available")
    return wrapper

@is_valid
def say_hi():
    print("Hello world!")


say_hi()