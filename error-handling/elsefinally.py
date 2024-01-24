user_input=input("enter a number")

try:
    number=float(user_input)
    print(number)

except Exception as E:
    print("exception generated is ", E)
    print("enter a valid number")

else:
    print("executed")

#finally will always run even if exception is there or not
finally:
    print("i am always executed")