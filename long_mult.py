# An implementation of long multiplication

def recursive_carry(multiplicand, multiplier):
    str_multiplier = str(multiplier)

    count = 1

    products = []

    trailing_zeros = ""

    while count <= len(str_multiplier):
        curr_multiplier = f"{str_multiplier[len(str_multiplier) - count]}{trailing_zeros}"
        products.append(int(curr_multiplier) * multiplicand)
        trailing_zeros = "0" * count
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