a = 1
b = 2

if a == b:
    print("a == b")

if a is b:
    print("a is b")

if type(a) is type(b):
    print("type(a) is type(b)")

if isinstance(a, type(b)):
    print("isinstance(a, type(b))")