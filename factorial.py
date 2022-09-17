# The Factorial, recursion example

def fact(n):
    # Base case
    if n <= 1:
        return 1
    res = n * fact(n - 1)
    return res

if __name__ == "__main__":
    res = fact(5)
    print(res)