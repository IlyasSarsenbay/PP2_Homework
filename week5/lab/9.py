import re
def match(text):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", text)
string = input()
print(match(string))