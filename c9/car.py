class Car:
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'

        return long_name.title()

    def read_odometer(self):
        print(f'this car has {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("ok, do it")


my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 25
my_new_car.read_odometer()

my_new_car.update_odometer(1)
my_new_car.read_odometer()

my_new_car.increment_odometer(2)
my_new_car.read_odometer()
