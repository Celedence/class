class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_eggs(self):
        self.eggs += 1
        Chicken.total_eggs +=1
        return self.eggs


c1 = Chicken("henrietta","white")
c2 = Chicken("clucky","not so white")
print(c1.lay_eggs())
print(c2.lay_eggs())
print(Chicken.total_eggs)