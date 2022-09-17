nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in nested_list:
    for j in i:
        print(j, end=" ")
    print("\n")

order = [
    ["Big Mac", 89.00, 3],
    ["Quarter Pounder", 102.99, 2],
    ["Chilli Cheese Fries", 56.00, 5]
]

for item in order:
    print(f"Product: {item[0]} Price: {item[1]} Quantity: {item[2]} \n")

order[2][1] = order[2][1] + 12

for item in order:
    print(f"Product: {item[0]} Price: {item[1]} Quantity: {item[2]} \n")