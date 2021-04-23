from datetime import date




class Pig:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
Alienor = Pig("Mr Alienor", "Pig", "noon" )
# Alienor.name = "Mr Alienor"
# Alienor.species = "Pig"
print(Alienor.__dict__)
print(f'{Alienor.name} the {Alienor.species} is available to pet during the {Alienor.shift} shift.')