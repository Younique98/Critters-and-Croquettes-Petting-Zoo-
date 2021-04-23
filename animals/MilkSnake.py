from datetime import date



class MilkSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
Huw = MilkSnake("Mr Huw", "domestic snake")
# Huw.name = "Mr Huw"
# Huw.species = "domestic snake"
print(Huw)