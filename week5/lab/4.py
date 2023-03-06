import re
def match(text):
        p = '[A-Z]+[a-z]+$'
        if re.search(p,  text):
                return 'match'
        else:
                return('Not match')
string = input()
print(match(string))