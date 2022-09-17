# Odd count Generator Function

def oddCount(min, max):
    while min <= max:
        yield min
        min += 2

# For Loop to print odd numbers

for i in oddCount(1, 10):
    print(i)

