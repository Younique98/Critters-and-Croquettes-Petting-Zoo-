from datetime import date



class BallPythonSnake:

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

Charlie = BallPythonSnake("Mr Charlie", "snake", "snake chow" )
# Charlie.name = "Mr Charlie"
# Charlie.species = "snake"
print(Charlie.feed())
