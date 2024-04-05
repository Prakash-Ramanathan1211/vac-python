class Person:
    name = "John Doe"
    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name 

p = Person()
print(p.getname())
p.setname("michael")
print(p.getname())