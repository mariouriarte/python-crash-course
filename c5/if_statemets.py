cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print((car.upper()))
    else:
        print(car.title())

# checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("hold the anchovies!")

# numerical comparisons
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

if 'bmw' in cars:
    print('Is in the list')

nissan = 'nissan'
if nissan not in cars:
    print(f'{nissan.title()}, Is not in the list')

# checking that a list in not empty
requested_toppings = []
if requested_toppings:
    for item in requested_toppings:
        print(f"Adding {item}")
    print("\nFinish making your pizza!")
else:
    print("Are you sure you want a plain pizza")

# multiple list
print("\nMultiple list")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for item in requested_toppings:
    if item in available_toppings:
        print(f"Adding {item}.")
    else:
        print(f"Sorry , we don't have {item}")
print("\nFinish making your pizza")

# others
float_number = 4.5
if float_number == 4.5:
    print(True)
