def iterTest(min, max):
    while min <= max:
        print(min)
        min += 1

def recursiveTest(min, max):
    if min <= 0:
        return 
    if min <= max:
        print(min)
        return recursiveTest(min + 1, max)

iterTest(0, 10)
recursiveTest(1, 10)