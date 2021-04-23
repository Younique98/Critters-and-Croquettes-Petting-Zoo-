from datetime import date




class Pig:

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

Alienor = Pig("Mr Alienor", "Pig", "noon", "fancy chow" )
# Alienor.name = "Mr Alienor"
# Alienor.species = "Pig"
print(Alienor.feed())
print(f'{Alienor.name} the {Alienor.species} is available to pet during the {Alienor.shift} shift.')