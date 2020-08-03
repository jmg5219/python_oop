# This is how you define a class
class Cat:
    species = "mammal"
    legs = "4"
    fur = "long hair"

    #This is a constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return "%s is %d years old" % (self.name, self.age)
    
    #Instance Method, every method pass self
    def eat(self,cans_of_food):
        self.cans_of_food = cans_of_food
        return "%s ate %d cans of food"%(self.name,self.cans_of_food)

#Guster is instance of Cat class
guster = Cat("Guster",10)
beans = Cat("Beans",11)
print(guster)
#calling the eat method on the cat class and can only apply to instance of class
# print(guster.eat(1))
# print(beans.eat(2))
