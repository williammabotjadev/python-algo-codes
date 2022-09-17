# Using __repr__ special methods to create a string representation

class custom_class(object):
    def __init__(self, greeting) -> None:
        self.greeting = greeting 

    def __repr__(self) -> str:
        return f"{self.greeting} custom class"

if __name__ == "__main__":
    inst = custom_class("Buenos Tardes")
    print(inst)
