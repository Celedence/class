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

class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return f"{self.full_name()} removed your post from the {self.community}"

jasmine = Moderator("Jasmine", "Connor", 61, "piano")

print(jasmine.full_name())
print(jasmine.likes("chips"))
print(jasmine.is_senior())
print(jasmine.remove_post())