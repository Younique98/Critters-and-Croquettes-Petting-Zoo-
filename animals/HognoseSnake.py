from datetime import date


class HognoseSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
Grace = HognoseSnake("Miss Grace", "Snake" )
# Grace.name = "Miss Grace"
# Grace.species = "Snake"
print(Grace)