import os
p = 'c:/Users/User/Desktop/pp2_homework/PP2_Homework-7'
print("directories:")
print([ x for x in os.listdir(p) if os.path.isdir(os.path.join(p, x)) ])
print("\nfiles:")
print([ x for x in os.listdir(p) if not os.path.isdir(os.path.join(p, x)) ])
print("\ndirectories and files:")
print([ x for x in os.listdir(p)])