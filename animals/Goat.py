from datetime import date

class Goat:
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True
        self.shift = ""
Lucy = Goat("Lucy", "goat", "morning" )
# Lucy.name = "Lucy"
# Lucy.species = "goat"
print(Lucy)
print(Lucy.name)
print(f'{Lucy.name} the {Lucy.species} is available to pet during the {Lucy.shift} shift.')
