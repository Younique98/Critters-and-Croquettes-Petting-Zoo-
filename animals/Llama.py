from datetime import date

class Llama:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = "midday"
Jess = Llama("Miss Fuzz", "domestic llama" )
# Jess.name = "Miss Fuzz"
# Jess.species = "domestic llama"
print(Jess)
print(f'{Jess.name} the {Jess.species} is available to pet during the {Jess.shift} shift.')