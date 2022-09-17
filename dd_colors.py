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

for color, status in dd.items():
    status_text = ""
    if status:
        status_text = "is primary"
    else:
        status_text = "is not primary"
    print(f"{color} {status_text}")