class Animal:
    # constructor:
    '''
    contructor execute while creating the object only once
    '''
    def __init__(self, name , age , species):
        self.name = name
        self.age = age
        self.species = species
        # self dot isiliye banayi taki ham variable dubara reuse or share kar sake new function me
        
    def speak(self):
        print(f'{self.name} is speaking ')

    def walk(self):
        print(f'{self.name} is walking')

# create an object for a human
human = Animal('aman' , '20' , 'Human')

# make your human speak
human.speak()

# make your human walk
human.walk()

#Hw create a class vehicle and take the attributes from the parameter in the constructor and add the relevent methods to it