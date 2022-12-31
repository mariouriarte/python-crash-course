import Restaurant

class IceCreamStand(Restaurant.Restaurant):

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.prepare(flavors)

    def prepare(self, flavors):
        self.flavors = flavors

    def get_flavors(self):
        print('Los sabares disponibles son:')
        for flavor in flavors:
            print(f'- {flavor}')

flavors = ['Canela', 'Sania', 'Chocolate']

frigo = IceCreamStand('Frigo', 'Heladeria', flavors)
frigo.get_flavors()
