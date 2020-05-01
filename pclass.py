class User:

    active_user = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_user +=1

    def logout(self):
        User.active_user -=1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]} {self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def age(self):
        return f"{self.age}"

    def birthday(self):
        self.age +=1
        return f"Happy {self.age}th birthday, {self.first}"

    @classmethod
    def set_active_user(cls, num):
        cls.active_user = num

user1 = User("annaelle","nubs", 34)
user2 = User("me","nubs", 34)
user3 = User("babes","nubs", 34)

User.set_active_user(5)

print(User.active_user)
print(user1.birthday())
print(user1.full_name())
print(user1.age)
print(User.active_user)