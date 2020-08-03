# This is how you define a class
class Car:
    engine = "1"
    tires = "4"
    
    #This is a constructor
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    #string representation of the object   
    def __str__(self):
        return "Make: %s Model: %s Year: %s" % (self.make, self.model, self.year)
    

#car1 is instance of Car class
car1 = Car("BMW","M3","2020")
print(car1)

