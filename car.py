# Class

class Car():
    def __init__(self, make, model, color): # self is always the first argument
        self.make = make
        self.model = model
        self.color = color
        self.gas = 100
    
    def __str__(self):
        return "{}, {}, {}".format(self.make, self.model, self.color)
    
    def drive(self):
        self.gas -= 10
        print(self.gas)

    def fillTank(self):
        self.gas = 100
        print("Gas is now full")

    def check_gas(self):
        print(f"Gas handle: {self.gas}")
    
car1 = Car("Toyota", "Prius", "Black")

print(car1) # returns <__main__.Car object at 0x7ff725a5dc10> IF def __str__(self) entry not created
print(car1.make) # returns Toyota
car1.drive()
car1.drive()
car1.drive()
car1.check_gas()
car1.drive()
car1.fillTank()