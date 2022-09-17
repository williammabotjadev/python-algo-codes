# OOP Introduction

class Employee(object):
    numEmployees = 0
    def __init__(self, name, rate) -> None:
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployees += 1

    def __del__(self):
        Employee.numEmployees -= 1 

    def hours(self, numHours):
        self.owed += numHours * self.rate 
        return f"{numHours} hours worked"

    def pay(self):
        self.owed = 0
        return f"Paid {self.name}"

class specialEmployee(Employee):
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate)
        self.owed = 0 
        self.bonus = bonus 

    def hours(self, numHours):
        self.owed = numHours * self.rate + self.bonus 
        return f"{numHours} hours worked"

if __name__ == "__main__":
    jack = Employee("Jack", 13.5)
    jill = Employee("Jill", 18.5)
    joe = specialEmployee("Joe", 20.5, 20)

    jill.hours(20)
    jack.hours(30)
    joe.hours(35)

    print(jill.owed)
    print(jack.owed)
    print(joe.owed)

    print(jack.pay())
    print(jill.pay())
    print(joe.pay())
    
    print(Employee.numEmployees)

    print(dir(jack))

    del jack 
    del jill 
    del joe 

    print(Employee.numEmployees)
