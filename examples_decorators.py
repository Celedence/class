from functools import wraps

def double_returns(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args,**kwargs)
        return val, val
    return wrapper

@double_returns
def add(x, y):
    return(x + y)

print(add(2,3))
# ===================

def ensure_fewer_than_three(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if args > 3
            raise ValueError ("must be 3 or less")
        return fn(*args, **kwargs)
    return wrapper