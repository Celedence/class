class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"A human named {self.first} {self.last}"

    def full_name(self):
        return f"Hi Im {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='newborn', last= self.last, age = 0)
        return "must be a human"

    def __mul__(self, other):
        if isinstance(other, int):
            return [self for i in range(other)]
        return "Cant multiply"


j = Human("brian","buen",45)
k = Human("babes","odn",43)
# print (j+k)
# print(j)
# print(k)
print(j*4)