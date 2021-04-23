from datetime import date

class KoiFish:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

Cameron = KoiFish("Miss Cameron", "Fish", "fish chow")
# Cameron.name = "Miss Cameron"
# Cameron.species = "Fish"
print(Cameron.feed())