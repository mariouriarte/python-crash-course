def is_number(number):
    if not number.isnumeric():
        raise ValueError(f'"{number}" is not a number')

def division(first, second):
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cant divide by 0!')
    else:
        print(answer)

# start
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

follow = True

while follow:
    try:
        first_number = input("\nFirst number: ")
        is_number(first_number)

        second_number = input("Second number: ")
        is_number(second_number)
    except ValueError as e:
        print(e)
    else:
        division(first_number, second_number)

    res = input('\nContinue y/n: ')
    if res == 'n':
        follow = False
