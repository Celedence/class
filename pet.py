class Pet:
    allowed = ["cat","dog","fish","rat"]
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError (f"You cant have a {species} pet")
        self.species = species
        
cat = Pet("Annabel", "fish")
dog = Pet("Peanut", "dog")

print(cat.name)
print(dog.species)