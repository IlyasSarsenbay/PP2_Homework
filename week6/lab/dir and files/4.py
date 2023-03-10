def len(fname):
        with open(fname) as f:
                for i, x in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",len("lab.txt"))