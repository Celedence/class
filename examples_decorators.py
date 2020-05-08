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