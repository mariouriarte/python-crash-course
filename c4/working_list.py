cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    print(car)

for car in cars:
    print(f"El carro elegido es {car.title()}")
    print(f"Este carro será utilizado {car.title()}")

# numerical list
print('rangos de 2 a 5')
for value in range(2, 5):
    print(value)

print('rangos 6')
for value in range(6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# set values in loop
squares = []
for item in range(1, 11):
    scuare = item ** 2
    squares.append(scuare)

print(squares)

# simple statics
digits = list(range(1, 10))
digits.append(0)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions
squares = [val**2 for val in range(1,11)]
print(squares)

# working whit a part of list
# slicing a list
print('slicing a list')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print('')
print(players[-3:])

# looping through a slice
for player in players[:3]:
    print(player)

# copying a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
players2 = players[:]

players.append('mario')

print(players)
print(players2)

