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

        