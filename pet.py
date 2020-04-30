class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

cat = Pet("Annabel", "cat")
dog = Pet("Peanut", "dog")

print(cat.name)
print(dog.species)