a = 20
b = 21

def f():
    global a 
    a = 21
    b = 21

f()
print(a)
print(b)