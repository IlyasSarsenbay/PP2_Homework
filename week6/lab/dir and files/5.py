stands = ['The World', 'The Hand', 'Crazy Diamond', 'Tusk', 'Big', 'Crimson']
with open('stand.txt', "w") as myfile:
        for c in stands:
                myfile.write("%s\n" % c)

content = open('stand.txt')
print(content.read())