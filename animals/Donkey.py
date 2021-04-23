from datetime import date

class Donkey:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
Paul = Donkey("Mr Paul", "Donkey", "midday" )
# Paul.name = "Mr Paul"
# Paul.species = "Donkey"
print(Paul.name)
print(f'{Paul.name} the {Paul.species} is available to pet during the {Paul.shift} shift.')