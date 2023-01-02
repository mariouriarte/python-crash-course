from pathlib import Path

path = Path('c10/text_files/pi_million_digits.txt')
contents = path.read_text()
# contents = contents.rstrip()

lines = contents.splitlines()

pi_string = ''

for line in lines:
    pi_string += line

print(f'{pi_string[:52]}...')
print(len(pi_string))
