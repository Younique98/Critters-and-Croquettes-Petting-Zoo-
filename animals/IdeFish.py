from datetime import date

class IdeFish:

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

Jack = IdeFish("Mr Jack", "Fish", "fish chow")
# Jack.name = "Mr Jack"
# Jack.species = "Fish"
print(Jack.feed())
