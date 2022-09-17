# CLass Methods

class Aexp(object):
    base = 2
    @classmethod
    def exp(cls, x):
        return(cls.base ** x)

class Bexp(Aexp):
    base = 3 

class Zexp(object):
    __base = 2
    def __exp(self):
        return(self.base ** 2) 
    
if __name__ == "__main__":
    exp = Aexp()
    print(exp.exp(2))

    bexp = Bexp()
    print(bexp.exp(2))

    z = Zexp()
    print(z.__exp())