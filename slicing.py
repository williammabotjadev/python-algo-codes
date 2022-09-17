status = "online"

print(status[0:4])
print(status[0:4:2])
print(status[0::2])
print(status[::-1])

# Index by Expression

print(status[::len(status) - 1])
print(status[1 + 2])

# Enumerate Characters

for i in enumerate(status[0:len(status)]):
    print(i)

# String Builder 

greeting = "hello world"

print(greeting[:5] + " wonderful" + greeting[5:])

