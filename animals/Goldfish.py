from datetime import date
class Goldfish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
Nat = Goldfish("Mr Nat", "Goldfish")
# Nat.name = "Mr Nat"
# Nat.species = "Goldfish"
print(Nat)