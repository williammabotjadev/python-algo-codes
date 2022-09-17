def double(x):
    return x * 2

def quad(x):
    return x * 4

lst = []

for i in range(16):
    lst.append(double(quad(i)))

print(lst)

print([double(x) for x in range(16) if x in [quad(y) for y in range(16)]])