from pathlib import Path
path = Path('c10/text_files/guest.txt')

name = input('Tell me you name: ')

path.write_text(name)
