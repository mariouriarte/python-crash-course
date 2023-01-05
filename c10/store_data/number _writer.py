from pathlib import Path
import json

# numbers = [1,2,3,4,6,8,9]
payload = {'first_name': 'Mario','second_name': 'Uriarte'}
contents = json.dumps(payload)

path = Path('c10/text_files/numbers.json')
path.write_text(contents)
