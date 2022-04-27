import os

#  my_file = open("C:\\Users\ASUS\Desktop\\text.txt", "r")
if os.path.exists("text.txt"):
    print('File found')
else:
    print('File not found')