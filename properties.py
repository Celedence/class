
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self.age = age
        else:
            self.age = 0

    def full_name(self):
        return f"{self.first} {self.last}"


    # @property
    # def age(self):
    #     return self.age

    # @age.setter
    # def age(self, value):
    #     if value >= 0:
    #         self.age = value
    #     else:
    #         raise ValueError ("Age must be a positve number")

human = Human("bob","smily", 45)
 
print(human.full_name())
