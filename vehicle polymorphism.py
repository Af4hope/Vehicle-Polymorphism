# Class 1
class BMW:
    def brand(self):
        print("BMW is a German luxury car manufacturer.")
    
    def fuel_type(self):
        print("BMW cars usually run on petrol or diesel.")
    
    def type(self):
        print("BMW produces luxury and performance cars.")

# Class 2
class Ferrari:
    def brand(self):
        print("Ferrari is an Italian sports car manufacturer.")
    
    def fuel_type(self):
        print("Ferrari cars usually run on high-octane petrol.")
    
    def type(self):
        print("Ferrari produces high-performance sports cars.")

# Object creation
obj_bmw = BMW()
obj_ferrari = Ferrari()

# Common interface (Polymorphism)
for car in (obj_bmw, obj_ferrari):
    car.brand()
    car.fuel_type()
    car.type()
    print("------------")
