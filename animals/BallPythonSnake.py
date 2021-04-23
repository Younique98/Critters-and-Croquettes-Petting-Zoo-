from datetime import date



class BallPythonSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
Charlie = BallPythonSnake("Mr Charlie", "snake" )
# Charlie.name = "Mr Charlie"
# Charlie.species = "snake"
print(Charlie)
