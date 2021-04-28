from OOP_notes.animal import Animal

class Reptile(Animal): # inheritence

    def __init__(self):
        super().__init__()  # initialize everything from animal class " Inheritence"
        self.cold_blooded = True

    def use_venom(self):
        print("if i have venom im going to use it")

    def moving(self):
        print("moves like a snake")  # polymorphism

    def __repr__(self):  # Give details about the class
        return f"This is a reptile"

    def __str__(self): # will change how info is represented(same as __repr__)
        return f"str version of this is reptile"


bob = Reptile()

print(repr(bob))
# or
print(bob) # if you have set __str__(self) then it will follow that format, if not then it will follow the __repr__ format.
