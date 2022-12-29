class Car:
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'

        return long_name.title()

    def read_odometer(self):
        print(f'this car has {self.odemeter_reading} miles on it')

my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.get_descriptive_name())

my_new_car.odemeter_reading = 25
my_new_car.read_odometer()
