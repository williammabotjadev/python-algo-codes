order = [
    ["Greek Salad", 84.00, 3],
    ["Chicken Wrap", 99.00, 2],
    ["Avocado", 78.00, 1]
]

sorted_order = sorted(order, key=lambda x: x[1])
order.sort(key=lambda x: x[1])

print(order)
print(sorted_order)