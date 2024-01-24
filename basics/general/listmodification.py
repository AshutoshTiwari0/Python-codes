people:list=["1","2","3","4"]

#note- we should never modify our list inside a loop
for i in people:
    if i=="2":
        people.remove("2")

    if i=="3":
        print("random")

print(people)