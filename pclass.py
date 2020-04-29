class User:
    def __init__(self, first, last, age):
        self.first = first,
        self.last = last,
        self.age = age


user1 = User("joe","mcman", 55)
user1 = User("annaelle","nubs", 34)
print(user1.first, user1.last, user1.age)