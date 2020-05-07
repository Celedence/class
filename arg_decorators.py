def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, im {name}"

@shout
def order(main, side):
    return f"I want a {main} and a side of {side}"

def lol():
    return "lol"

print(greet("brian"))

print(order("burger","fries"))

print(lol())

#==========
def log_function_data(fn):
    def wrapper(*args, **kwargs):
        print(f"you are calling the {fn.__name__} function")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    """Adds 2 numbers together"""
    return x + y

print(add(23, 23))