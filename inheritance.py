class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def printdetails(self):
        print("name= " + self.name + " age=" + str(self.age) )

class Student(Person):

    pass 

x = Student("Thiru",19)
x.printdetails()

         