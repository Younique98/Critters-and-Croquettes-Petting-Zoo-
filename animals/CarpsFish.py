from datetime import date

class CarpsFish:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

Elizabeth = CarpsFish("Miss Elizabeth", "Fish", "fish chow" )
# Elizabeth.name = "Miss Elizabeth"
# Elizabeth.species = "Fish"
print(Elizabeth.feed())