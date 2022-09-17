# defaultdict bool demo

from collections import defaultdict

dd = defaultdict(bool)

def isprimary(color):
    if color.casefold() == "red".casefold() or color.casefold() == "green".casefold() or color.casefold() == "blue".casefold():
        return True 
    else:
        return False 
    
s = "Red Green Blue Purple Yellow Pink Black White"

colors = s.split()

for color in colors:
    dd[color] = isprimary(color)

print(dd)