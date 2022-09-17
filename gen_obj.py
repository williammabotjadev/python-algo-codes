# Create a Generator Object

lst = [1, 2, 3, 4, 5]

gen_obj = (i ** 2 for i in lst)

for x in gen_obj:
    print(x)