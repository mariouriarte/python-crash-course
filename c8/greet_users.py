def greet_users(list_name):
    """Print a simple greeting to each user in the list."""
    for name in list_name:
        print(f'hello {name.title()}')

    # del names[0]

names = ['mario', 'carla', 'carmen']

greet_users(names[:])

print(names)
