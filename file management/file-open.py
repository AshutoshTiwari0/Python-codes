"""
with open('file management\\fileread.txt', 'r') as text:
    #print(text.read())

    list_of_content:list[str]=text.readlines()
    print(list_of_content)
"""

#writing in a file
with open('file management\\fileread.txt','a+') as text:
    #text.write("\n a new line added by python code")
    text.write("\n soon i will start data science")
    print(text.read())


#write()-> it chnages the entire content of the file with whatever we write in ()
    
#with keyword closes the file automatically
