class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f'This restaurant name is {self.name} and type is {self.cuisine_type}' )

    def ope_restaurant(self):
        print('The restaurant is open')

# pollo_loco = Restaurant('Pollo loco', 'Roticeria')
# pollo_loco.describe()
# pollo_loco.ope_restaurant()
