FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

def delete_blank_line(todos_arg,filepath=FILEPATH):
    """ Delete blanks at the end of a to-do items list """
    for index, items in enumerate(todos_arg):
        if items == '\n':
            todos_arg.remove('\n')
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == '__main__':
    print('Hello ...from functions')
    print(get_todos())