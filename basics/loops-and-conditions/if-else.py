"""
a=101

if a%2==0:
    print("Number is even")

else:
    print("number is odd")
print("no indent means i am out of if block")
"""

"else if statements->in python it is known as elif"


text="Write a rap bar in English"
if text=="Hello":
    print("Hey!.How can i Help you?")
elif text=="Write a rap bar in Hindi":
    print("""They see me winning i am maxed out
          aur le rha mai victory laps now
          imma just put them in choke hold
          karne ye lagege Tap Out, Tap Out""")
elif text=="Write a rap bar in English":
    print("""I'm 'bout to
Smash into everyone 
Crash into everything
Back and i've just begun, fack 2017
Smash into evreyone
Crash like an F-15
Damage already done
Y'all should have let me be
-Eminem Kamakaze""")
else:
    print("Error")


# A shorcut way of if else
# Ternary operator in other languages.
print("number is even") if(10%2==0) else print("Number is odd")
# true statement || condition || false statement

a,b=10,20  # this tells that a=10 and b=20
print("A is greater") if a>b else print("B is greater")

p,q=15,7
bigger= p if p>q else q
print(bigger)
    