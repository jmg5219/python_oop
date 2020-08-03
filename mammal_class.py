class Mammal:
    # constructor
    def __init__(self,name,type_of_mammal,breed,legs):
        self.name = name
        self.type_of_mammal = type_of_mammal
        self.breed = breed
        self.legs = legs

    def eat(self):
        return "%s is eating" % (self.name)

#Class Cat is an extension of class mammal, creates a new class called cat and extends all the properties of mammal to cat
class Cat(Mammal):
    def __init__(self, name, type_of_mammal, breed, legs, fur):
        #super method, init off the super method
        super().__init__(name, type_of_mammal,breed,legs)
        self.fur = fur
    
    def __str__(self):
        return "%s is a %s %s with %d legs and %s fur" % (self.name,self.type_of_mammal,self.breed,self.legs,self.fur)

    def purr(self):
        return "%s is purring" % (self.name)
    
    def eat(self):
        return "THE CAT EATS DIFFERENTLY FOR REASONS!"

guster = Cat("Gus","cat","mixed",4,"short hair")
harry = Mammal("Harry","Dog","lab",4)
print(guster)
print(guster.eat())
print(guster.purr())
print(harry.eat())

# print(guster.eat())