# You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.
#
# Examples:
#
# uniTotal("a") == 97
# uniTotal("aaa") == 291

def uni_total(s):
    total: int = 0
    for i in s:
        total += ord(i)
    return total

# best practices
# def uni_total(string):
#     return sum(map(ord, string))
# or
# def uni_total(s):
#     return sum(ord(c) for c in s)


