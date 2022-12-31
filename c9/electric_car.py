# from car import Car as Car
import car
import battery

class ElectricCar(car.Car):
    '''Represent aspects od a car, specific to electric vehicles'''

    def __init__(self, make, model, year=2022):
        super().__init__(make, model, year)
        self.battery = battery.Battery(65)

    def describe_battery(self):
        self.battery.describe_battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf')

print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()

my_leaf.battery.get_range()
