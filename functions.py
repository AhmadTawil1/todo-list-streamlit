FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg ,filepath=FILEPATH):
    """ Write the to-do item list in the text file.
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
