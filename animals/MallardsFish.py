from datetime import date
class MallardsFish:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

Aimee = MallardsFish("Miss Aimee", "MarllardsFish", "fish chow")
# Aimee.name = "Miss Aimee"
# Aimee.species = "MarllardsFish"
print(Aimee.feed())