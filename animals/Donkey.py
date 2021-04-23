from datetime import date

class Donkey:

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

Paul = Donkey("Mr Paul", "Donkey", "midday", "fancy chow" )
# Paul.name = "Mr Paul"
# Paul.species = "Donkey"
print(Paul.feed())
print(f'{Paul.name} the {Paul.species} is available to pet during the {Paul.shift} shift.')