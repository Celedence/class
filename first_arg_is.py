from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wrap(fn)
        def wrapper(*arg, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg_is("steak")
def fav_foods(*foods):
    print(foods)
