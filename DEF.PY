class person:
    def __init__(self, name):             
        self.name = name

    def talk(self):
        print(f"Hi, Iam {self}")


john = person("John Smith")
john.talk()
bob = person("bob smith")
bob.talk()