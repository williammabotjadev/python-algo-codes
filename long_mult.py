# An implementation of long multiplication

def recursive_carry(multiplicand, multiplier):
    str_multiplier = str(multiplier)

    count = 1

    products = []

    while count <= len(multiplier):
        products.append(multiplier[len(multiplier) - count] * multiplicand)
        count += 1 

    sum = 0 

    for i in products:
        sum += i 

    return sum 

def long_mult(x, y):
    if(x > y):
        multiplicand = x
        multiplier = y 
    else:
        multiplicand = y
        multiplier = x 

    res = recursive_carry(multiplicand, multiplier)

    return res
    
if __name__ == "__main__":
    print(long_mult(23423, 4892))