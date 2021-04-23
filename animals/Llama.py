from datetime import date

class Llama:

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

    def __str__(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

Jess = Llama("Miss Fuzz", "domestic llama", "midday", "fancy chow" )
# Jess.name = "Miss Fuzz"
# Jess.species = "domestic llama"
print(Jess.__str__())
print(f'{Jess.name} the {Jess.species} is available to pet during the {Jess.shift} shift.')