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

# Get sorted list of keys

sorted_keys = sorted(list(d))

print(sorted_keys)

sorted_vals = sorted(list(d.values()))

print(sorted_vals)

sorted_by_vals = sorted(list(d), key=d.__getitem__)

print(sorted_by_vals)

sort_by_comp = [v for (k,v) in sorted(d.items())]

print(sort_by_comp)

sort_by_vals_rev = sorted(list(d), key=d.__getitem__, reverse=True)

print(sort_by_vals_rev)

d_one = {
    "one": "uno",
    "two": "deux",
    "three": "trois",
    "four": "quadre",
    "five": "sinq",
    "six": "six"
}

sorted_bilingual = sorted(d_one, key=d.__getitem__)

print(sorted_bilingual)

sorted_bilingual_comp = [d_one[i] for i in sorted(d_one, key=d.__getitem__)]

print(sorted_bilingual_comp)