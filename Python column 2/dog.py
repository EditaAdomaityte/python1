class Dog:
    species = "Canis familiaris"
    def __init__(self,name, age):#define the properties that all Dog objects,__init__sets the initial state of the object by assigning the values of the object’s properties
        self.name=name
        self.age=age

miles=Dog("Miles",4)
buddy=Dog("Buddy",9)