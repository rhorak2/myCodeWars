# Write a function that returns a string in which firstname is swapped with last name.
#
# Example(Input --> Output)
#
# "john McClane" --> "McClane john"

def name_shuffler(str_):
    name = str_.split()
    return name[1] + " " + name[0]

# best practices
# def name_shuffler(str_):
#     return ' '.join(str_.split(' ')[::-1])
