from datetime import date


class RatSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
Yvee = RatSnake("Miss Yvee", "Snake")
# Yvee.name = "Miss Yvee"
# Yvee.species = "Snake"
print(Yvee)