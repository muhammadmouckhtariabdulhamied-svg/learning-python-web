class mammal:
    def bark(self):
        print("bark")


class Dog(mammal):
    def be_annoying(self):
        print("annoying")
    

class cat(mammal):
    pass

dog1 = Dog()
dog1.bark()