"""
Calculates the the time it takes to calculate the sum of a list using generators vs. using lists
"""

import time 

# Generator Function 

def oddGen(min, max):
    while min <= max:
        yield min 
        min += 2 

# List Function
def oddList(min, max):
    lst = []
    while min <= max:
        lst.append(min)
        min += 2
    return lst

# Generator Function Performance
start = time.time()
sum(oddGen(0, 100000000))
end = time.time()
print("Generator Function Performance: ", end - start)

# List Function Performance
start = time.time()
sum(oddList(0, 100000000))
end = time.time()
print("List Function Performance: ", end - start)

