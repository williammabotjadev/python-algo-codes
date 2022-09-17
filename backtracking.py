# An Example of using the backtracking technique

def perms(n, word):
    if n == 1:
        return word 
    return [digit + bits for digit in perms(1, word) for bits in perms(n - 1, word)]

if __name__ == "__main__":
    print(perms(len("abc"), "abc"))

    