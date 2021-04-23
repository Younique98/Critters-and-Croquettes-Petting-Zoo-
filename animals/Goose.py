from datetime import date


class Goose:

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

Oscar = Goose("Mr Oscar", "domestic goose", "afternoon", "fancy chow" )
# Oscar.name = "Mr Oscar"
# Oscar.species = "domestic goose"
print(Oscar.feed())
print(f'{Oscar.name} the {Oscar.species} is available to pet during the {Oscar.shift} shift.')