gametag="Controller Kid"
gaming_name:str=f"Hello my gamimg name is {gametag}. I used to play call of duty mobile where my username was {gametag}"

# :5 tells to take 5 spaces
print(gaming_name)
print(f'{gametag:5} after space')
print(f'{gametag:>20}')# pushes name to right with 20 spaces
print(f'{gametag:<20}') # pushes to left
print(f'{gametag:^20}') # pushes to center


number=10_000.123456

#rounds to two decimal places
print(f'{number:.2f}')

num2=1_000_000
print(f'{num2:.0e}')