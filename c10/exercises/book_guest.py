from pathlib import Path

print('Tell me a list of names, press n to exit')

follow = True
names = []

while follow:
    name = input('Input name (n to exit): ')

    if name == 'n':
        follow = False
    else:
        names.append(name)

content = ''
for name in names:
    content += name + '\n'

path = Path('c10/text_files/guest_book.txt')
path.write_text(content)
