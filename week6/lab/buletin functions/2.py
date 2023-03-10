def string_test(s):
    d={"UP":0, "LOW":0}
    for c in s:
        if c.isupper():
           d["UP"]+=1
        elif c.islower():
           d["LOW"]+=1
        else:
           pass
    print ("Upper: ", d["UP"])
    print ("Lower: ", d["LOW"])

str=input()
string_test(str)