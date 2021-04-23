from datetime import date

class CopperheadsSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
Juliet = CopperheadsSnake("Miss Juliet", "Snake" )
# Juliet.name = "Miss Juliet"
# Juliet.species = "Snake"
print(Juliet)
