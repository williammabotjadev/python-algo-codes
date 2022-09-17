# CLass Methods

class Aexp(object):
    base = 2
    @classmethod
    def exp(cls, x):
        return(cls.base ** x)

class Baexp(Aexp):
    base = 3 

if __name__ == "__main__":
    exp = Aexp()
    print(exp.exp(2))

    bexp = Baexp()
    print(bexp.exp(2))