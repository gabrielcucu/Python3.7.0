class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def AboutPerson(self):
        print("Ma numesc "+self.name+" si am varsta de "+ str(self.age) +" ani.")