# """Este código sirve para tal"""

# def greet_user(username):
#     '''Display a simple greeting'''
#     print(f'Hello {username.title()}!')
    
# greet_user('Mario')

# #####

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)
