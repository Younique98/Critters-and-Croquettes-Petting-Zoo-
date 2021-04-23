from datetime import date


class Goose:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
Oscar = Goose("Mr Oscar", "domestic goose", "afternoon" )
# Oscar.name = "Mr Oscar"
# Oscar.species = "domestic goose"
print(Oscar)
print(f'{Oscar.name} the {Oscar.species} is available to pet during the {Oscar.shift} shift.')