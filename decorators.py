def be_polite(fn):
    def wrapper():
        print("what a pleasure to meet you")
        fn()
        print("have a great day")
    return wrapper

def greet():
    print("hi my name b")

def rage():
    print("i hate you")

greet = be_polite(greet)

greet()

polite_rage = be_polite(rage)

polite_rage()
# @decorator
def be_polite(fn):
    def wrapper():
        print("what a pleasure to meet you")
        fn()
        print("have a great day")
    return wrapper

@be_polite
def greet():
    print("my name is brian")

@be_polite
def rage():
    print("i hate you")

greet()
rage()
