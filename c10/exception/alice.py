from pathlib import Path

def count_words(path):
    '''Count the approximate number of words in a file.'''
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f'Sorry, the file {path} does not exist.')
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has about {num_words} words.')

books = ['alice.txt', 'asd.txt']

for book in books:

    path = Path(f'c10/text_files/{book}')
    count_words(path)
