from datetime import date

class Goat:
    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

Lucy = Goat("Lucy", "goat", "morning", "fancy chow" )
# Lucy.name = "Lucy"
# Lucy.species = "goat"
print(Lucy.feed())
print(Lucy.name)
print(f'{Lucy.name} the {Lucy.species} is available to pet during the {Lucy.shift} shift.')
