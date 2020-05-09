from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner
# decrator that accepts an argument
@ensure_first_arg_is("steak")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito","chips"))
print(fav_foods("steak","chips"))

# ===========================

def enforce(*type):
    def wrapper(fn):
        def new_func(*args, **kwargs):
            new_list = []
            for (a, b) in zip(args, types):
                new_list.append(a(b))
            return fn(*new_list,**kwargs)
        return new_func
    return wrapper

@enforce(str, int)
def repeat(msg, time):
    for time in range(time):
        print(msg)