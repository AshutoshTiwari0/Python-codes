import requests as r
from dataclasses import dataclass


@dataclass
class Quotes:
    quote:str
    author:str

url= "https://api.quotable.io/quotes/random"

def get_quote(url):
    request: r.Response = r.get(url=url)
    data_list: list = request.json()
    
    # Check if the list is not empty
    if data_list:
        # Access the first dictionary in the list
        data = data_list[0]

        # Uncomment the following line for debugging or inspection
        # print(data)
        
        content = data.setdefault("content", "...")
        author = data.setdefault("author", "...")
        
        return Quotes(content, author)
    else:
        return Quotes("No quote available", "Unknown author")

if __name__=="__main__":
    url="https://api.quotable.io/quotes/random"


    for i in range(3):
        quote=get_quote(url)
        print("quote is "+str(quote.quote))
        print("written by "+str(quote.author))
