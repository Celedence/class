
def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(3,cube))
print(sum(3,square))
# cubing 3 cubing 2 cubing 1 and adding them together

#nested function
from random import choice

def greet(person):
    def get_mood():
        msg = choice (('Hello there','Go away','I hate you'))
        return msg
    
    result = get_mood()+ person
    return result

print(greet("Toby"))
