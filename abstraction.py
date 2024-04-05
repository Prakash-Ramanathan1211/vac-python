from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def subject():
        pass 

class Maths(Subject):

    def subject(self):
        print("subject is maths")
        # pass

class Science(Subject):
    def subject(self):
        # pass
        print("subject is sci")

math = Maths()
math.subject()

