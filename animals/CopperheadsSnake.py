from datetime import date

class CopperheadsSnake:

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

Juliet = CopperheadsSnake("Miss Juliet", "Snake", "snake chow" )
# Juliet.name = "Miss Juliet"
# Juliet.species = "Snake"
print(Juliet.feed())
