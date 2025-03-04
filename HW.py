class Vehicle:
    def __init__(self,name,year,brake):
        self.name = name
        self.year = year
        self.brake = brake
    
    def accel(self):
        print(f'{self.name} {self.year} speed is 270 kmph')

    def start(self):
        print(f'{self.name} {self.year} can start quickly')
    
    def stop(self):
        print(f'{self.name} {self.year} can stop quickly')


car = Vehicle('bugatti' , 2017 , 'Best')
        
car.accel()
car.start()
car.stop()

class Honda(Vehicle):
    def __init__(self,name,model,year,fueltank,brake):
        super().__init__(name,year,brake)
        self.fueltank = fueltank
        self.model = model

    def capacity(self):
        print(f'{self.model}  holds {self.fueltank} ')
    
    def rotate(self):
        print(f'{self.model} has 7 rpm ')


car = Honda('honda','Amaze',2017, '5 litre','Good')
car.capacity()
car.rotate()
    
class Ferrari(Honda):
    def __init__(self, name, model, year, fueltank, brake,handbrake,steeringwheel):
        super().__init__(name, model, year, fueltank, brake)
        self.handbrake = handbrake
        self.steeringwheel = steeringwheel

    def stop(self):
        print(f'{self.name} can stop quickly using {self.handbrake} handbrake')

    def control(self):
        print(f'{self.name} has good perfomance {self.steeringwheel} steering wheel.')

car3 = Ferrari('Ferrari', '488 GTB' , 2022, '80 liters', 'Excellent', 'Electronic','racing-style')
car3.accel()
car3.stop()
car3.control()
    
class Lamborghini(Ferrari):
    def __init__(self, name, model, year, fueltank, brake, handbrake, steeringwheel,doors,safety_features):
        super().__init__(name, model, year, fueltank, brake, handbrake, steeringwheel)
        self.doors= doors
        self.safety_features = safety_features

    def open_doors(self):
        print(f'{self.name} has {self.doors} which opens upwards. ')

    def safety(self):
        print(f'{self.name} comes with {self.safety_features} for maximum safety')

carL = Lamborghini('Lamborghini', 'Venino','2011','85 liters','Excellent','carbon fibre','sports type' ,'Scissor','airbags') 
carL.open_doors()
carL.safety()
carL.stop()