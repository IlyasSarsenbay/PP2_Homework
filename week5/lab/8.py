import re
def match(text):
    return re.findall('[A-Z][^A-Z]*', text)
string = input()
print(match(string))