class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

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

user1 = User("joe","mcman", 55)
user2 = User("annaelle","nubs", 34)

print(user1.birthday())
print(user1.full_name())
print(user1.age)
print(user1.is_senior())