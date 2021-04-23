from datetime import date


class RatSnake:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


Yvee = RatSnake("Miss Yvee", "Snake", "snake chow")
# Yvee.name = "Miss Yvee"
# Yvee.species = "Snake"
print(Yvee.feed())