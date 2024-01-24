#file= open(r"C:\Users\Dell\Desktop\python codes\basics\test.txt")
"""
file= open("C:\\Users\\Dell\\Desktop\\python codes\\basics\\test.txt")
text=file.read()
print(text)
file.close()
"""

# i ran into an error known as unicode error. Fix->
#fix 1 is to just write "r" outside the path
# fix 2 is to use \\ everwhre as in line 2.


# method 2 for reading a file->using with keyword
# method 2 is preferred-> by using "with" keyword our file will automatically be closed. so we dont have to close it manually

with open(r"C:\Users\Dell\Desktop\python codes\basics\test.txt") as file:
    text=file.read()
    print(text)
