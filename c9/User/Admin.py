from User import User as User

class Admin(User):

    def __init__(self, first_name, last_name, dateof_birth):
        super().__init__(first_name, last_name, dateof_birth)
        self.initialize()

    def initialize(self):
        roles = ['ROLE_ADD_POST', 'ROLE_DELETE_POST', 'ROLE_BAN_USER']
        for rol in roles:
            self.roles.append(rol)


mario = Admin('Mario', 'Uriarte', '1984-11-14')
mario.describe_user()
mario.greet_user()
mario.show_privileges()
