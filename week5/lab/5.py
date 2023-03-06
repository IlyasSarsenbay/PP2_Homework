import re
def match(text):
        p = 'a.*?b$'
        if re.search(p,  text):
                return 'match'
        else:
                return('Not match')
string = input()
print(match(string))