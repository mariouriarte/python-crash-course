alien_0 = {'color': 'green', 'points': 5}

print(alien_0.get('color'))
print(alien_0.get('points'))

print(f"You just earned {alien_0['points']} points")

alien_0['points'] = 25

print(f"You just earned {alien_0['points']} points")

del alien_0
alien_0 = {}
alien_0['color'] = 'blue'
alien_0['points'] = 1

print(alien_0)

alien_0['speed'] = 'fast'
print(alien_0)

del alien_0['speed']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print(favorite_languages)

mario_language = favorite_languages.get('mario', 'No language value assigned')
print(mario_language)

# looping through dictionary
print("\looping through dictionary")
for key, item in favorite_languages.items():
    print(f"\nKey: {key}")
    print(f"Value: {item}")

# looping through keys in a dictionary
print("\nLooping through keys in a dictionary")
for key in favorite_languages.keys():
    print(key.title())

print('same:')

for key in favorite_languages:
    print(key.title())

# Looping Through a Dictionary’s Keys in a Particular Order
print("\nLooping Through a Dictionary’s Keys in a Particular Order")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()} thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print('\nLooping Through All Values in a Dictionary')
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# without repeat
print('\nwithout repeat')
for language in set(favorite_languages.values()):
    print(language.title())

print('\nwithout repeat')
languages = {'python', 'rust', 'python', 'c'}
print(languages)

# nesting
print('\nNesting')
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

del aliens
aliens = []

for number in range(30):
    new_alien = {'color': 'green', 'points': number, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
