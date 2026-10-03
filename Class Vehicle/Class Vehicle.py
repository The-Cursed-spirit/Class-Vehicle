# create class
class Vehicle:

    # create init method
    def __init__(self, max_speed, milage):

        #bind the argument
        self.max_speed = max_speed
        self.milage = milage

# Object creation
modelX = Vehicle(240, 18)

# access the variables inside init method
print("Model Max Speed : ", modelX.max_speed)
print("MOdel Mileage : ", modelX.milage)