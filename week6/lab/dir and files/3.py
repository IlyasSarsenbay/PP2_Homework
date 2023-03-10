import os
print("Test a path exists or not:")
path = r'c:/Users/User/Desktop/pp2_homework/PP2_Homework-7'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
path = r'c:/Users/User/Desktop/pp2_homework/PP2_Homework-8'
print("\n",os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))