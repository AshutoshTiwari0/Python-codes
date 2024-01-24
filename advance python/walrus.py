"""
def get_length(text:str):

    return len(text)

length=get_length("AShutosh")
print(length)


"""


"""
# walrus operator is this->  :=


def get_length(text)-> dict:
    words=text.split()
    total_words=len(words)
    return {"text":text,
            "length of text is":(length := len(text)),
            "words":words,
            "total_words":(total_words),
            "avg_words":(avg:= total_words /len(words))
            }

for key,value in get_length("Hey this is a walrus operator").items():
    print(key, value,sep="||")
"""

# example 2-> walrus

if __name__=="__main__":
    while user_input:= input("enter text"):
        print(user_input)
    print("done")


#walrus is used for assigning a variable inside a loop
    #symbol->   :=






