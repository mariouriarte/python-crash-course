
print('\nSize of book in inches (8.5 x 0.3 x 11)')

def convert_in_cm(size):
    sizes = size.split(' x ')

    base = float(sizes[0])
    deep = float(sizes[1])
    high = float(sizes[2])

    base *= 2.54
    deep *= 2.54
    high *= 2.54

    print(f'\nDimensions whit deep in cm are: {base} x {deep} x {high}')
    print(f'Dimensions in cm are: {base} x {high}')


size = input('Enter size:')
convert_in_cm(size)
