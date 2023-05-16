from name_function import get_formatted_name

def test_first_last_name():
    '''Do names like Janis Jopling'''
    formatted_name = get_formatted_name('janis', 'arturo', 'joplin')

    assert formatted_name == 'Janis Arturo Joplin'
