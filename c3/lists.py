bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)

print(f"my first bicycle was a {bicycles[0].title()}")

message = f"este es un mensaje para una bicicleta {bicycles[1].title()}"
print(message)

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])

print(len(bicycles))

# add element a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print('add element a list')
print(motorcycles)

# insert element a list
motorcycles.insert(0, 'bmw')
print('insert element a list')
print(motorcycles)

# remove element of list
del motorcycles[0]
print('remove element of list')
print(motorcycles)

# removing an item using pop, remove last item of list and set in new var
print('removing an item using pop')
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# remove any element and save
print('')
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycles)

# remove item by value
print('remove item by value')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

# sorting a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sorting a list reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# tempotal order list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))

# printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# printing length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

print(cars[len(cars)-1])
