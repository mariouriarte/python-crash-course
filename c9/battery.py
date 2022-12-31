class Battery:
    '''A simple attempt to model a battery for an electric car.'''
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'this car has a {self.battery_size}-KWh battery')

    def get_range(self):
        '''Print a statemnet about the range'''
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f'This car can go about {range} miles on a full charge')
