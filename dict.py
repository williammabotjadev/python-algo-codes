# A demo of Dictionaries

d = {
    "one": 1,
    "two": 2,
    "three": 3
}

print(d)

d["four"] = 4 

print(d)

d.update({
    "five": 5, 
    "six": 6
})

print("five" in d)

print(d)