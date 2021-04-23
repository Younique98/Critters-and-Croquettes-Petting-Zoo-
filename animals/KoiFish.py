from datetime import date

class KoiFish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
Cameron = KoiFish("Miss Cameron", "Fish")
# Cameron.name = "Miss Cameron"
# Cameron.species = "Fish"
print(Cameron)