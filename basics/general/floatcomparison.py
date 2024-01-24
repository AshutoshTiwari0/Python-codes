"""
a=0.3
b=0.1+0.2# this gives the output->0.30000000000000004. we get so many zeros due to processing of computer

print(a)
print(b)
print(a==b)
"""

#way for comparison

def comparison(a,b,tolerance):
    absolute=abs(a-b)
    #absolute always give a +ve value
    print(f"{a}-{b}={a-b}")
    return absolute<tolerance

first=0.9
second=0.8+0.200000000000000001
print(comparison(first,second,1e-10))
