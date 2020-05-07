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