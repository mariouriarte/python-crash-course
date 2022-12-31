class User:

    roles = ['ROLE_USER']

    def __init__(self, first_name, last_name, dateof_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.dateof_birth = dateof_birth

    def describe_user(self):
        print(f'\nInformation of user:')
        print(f'Full name: {self.full_name()}, date of birth: {self.dateof_birth}')

    def greet_user(self):
        print(f'Greetings user {self.full_name()}')

    def full_name(self):
        return self.first_name.title() + ' ' + self.last_name.title()

    def show_privileges(self):
        print(self.roles)

# mario = User('Mario', 'Uriarte', '1984-11-14')
# mario.describe_user()
# mario.greet_user()
