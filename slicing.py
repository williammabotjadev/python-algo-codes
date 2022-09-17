status = "online"

print(status[0:4])
print(status[0:4:2])
print(status[0::2])
print(status[::-1])

# Index by Expression

print(status[::len(status) - 1])
print(status[1 + 2])