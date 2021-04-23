from datetime import date
class MallardsFish:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

Aimee = MallardsFish("Miss Aimee", "MarllardsFish")
# Aimee.name = "Miss Aimee"
# Aimee.species = "MarllardsFish"
print(Aimee)