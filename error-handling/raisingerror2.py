def connection():
    is_connected:bool=False

    if not is_connected:
     raise Exception("no connection")
    else:
        print("everything works fine")
    
try:
   connection()
except Exception as e:
   print(e)