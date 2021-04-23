from datetime import date

class IdeFish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
Jack = IdeFish("Mr Jack", "Fish")
# Jack.name = "Mr Jack"
# Jack.species = "Fish"
print(Jack)
