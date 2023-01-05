from pathlib import Path
import json

path = Path('c10/text_files/numbers.json')

contents = path.read_text()
numbers = json.loads(contents)
print(numbers)
