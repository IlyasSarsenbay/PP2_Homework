import re
def match(text):
    return ''.join(x.capitalize() or '_' for x in text.split('_'))
string = input()
print(match(string))