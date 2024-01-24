

user_input=input("enter a valid even number ")

try:
    user_input=int(user_input)
 
    if user_input%2==1:
        raise Exception("told you to enter an even number")
    else:
        print("inputted number", user_input)

except ValueError as ve:
    print("error is", ve)

except Exception as e:
    print("exception is",e)



