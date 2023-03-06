import re
def match(text):
        p = 'ab{2,3}'
        if re.search(p,  text):
                return 'match'
        else:
                return('Not match')
string = input()
print(match(string))