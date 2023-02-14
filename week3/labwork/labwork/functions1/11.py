def pal(w):
    if w == w[::-1]:
        return True
    else:
        return False
w=input()
w=w.lower()
print(w)
print(pal(w))