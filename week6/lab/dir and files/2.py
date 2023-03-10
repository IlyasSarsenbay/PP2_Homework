import os
print('Exist:', os.access('c:/Users/User/Desktop/pp2_homework/PP2_Homework-7/week6/lab/dir and files/7.py', os.F_OK))
print('Readable:', os.access('c:/Users/User/Desktop/pp2_homework/PP2_Homework-7/week6/lab/dir and files/7.py', os.R_OK))
print('Writable:', os.access('c:/Users/User/Desktop/pp2_homework/PP2_Homework-7/week6/lab/dir and files/7.py', os.W_OK))
print('Executable:', os.access('c:/Users/User/Desktop/pp2_homework/PP2_Homework-7/week6/lab/dir and files/7.py', os.X_OK))