from datetime import date

class CarpsFish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
Elizabeth = CarpsFish("Miss Elizabeth", "Fish" )
# Elizabeth.name = "Miss Elizabeth"
# Elizabeth.species = "Fish"
print(Elizabeth)