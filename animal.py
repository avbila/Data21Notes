class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breathe in and one out")

    def eat(self):
        print("nom nom nom")

    def moving(self):
        print("frowrds, backwards and side to side")

if __name__ == "__main__": #  Used to make sure that this is run only when you run the original script.
    cat = Animal()
    cat.breathe()