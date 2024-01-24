# assert is a keyword which is used to catch errors
def get_str(data:str):
    print(data)
    assert isinstance(data,str),"data provided is not of type string"

get_str("Ashutosh")