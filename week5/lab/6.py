import re
def match(text):
    return re.sub("[ ,.]", ":", text)
string = input()
print(match(string))