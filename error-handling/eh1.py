"""
user_input=input("enter a number:")

try:
    number=float(user_input)
    print(number)
except:
    print("something went wrong")

"""
#how to handle an exception properly
"""
user_input=input("enter a number:")

try:
    number=float(user_input)
    print(number)
except Exception as e:
    print("an exception generated-"+str(e))

    """
#getting specific with errors
user_input=input("enter a number:")

try:
    number=float(user_input)
    print(number)
    result=number/0
    print(result)
except ValueError:
    print("enter a valid number")
except ZeroDivisionError:
    print("Can not divide by zero")
#general exception-> all other will come here
except Exception:
    print("something went wrong")



