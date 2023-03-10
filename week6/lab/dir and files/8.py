import os
if os.path.exists("c:/Users/User/Desktop/pp2_homework/PP2_Homework-7/week6/lab/dir and files/demo.txt"):
  os.remove("demo.txt")
else:
  print("The file does not exist")