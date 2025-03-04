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

    def run(self):
        print(f'{self.name} is running')

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name, age,"Dog")
        self.breed = breed

    def bark(self):
        print(f'{self.name} is barking')
    
# Now we create object of the class dog
golden_retreiver = Dog('oreo' , 5 , 'goldenretreiver')

golden_retreiver.bark()

golden_retreiver.walk()
        

# create an object for a human
human = Animal('aman' , '20' , 'Human')

# make your human speak
human.speak()

# make your human walk
human.walk()



#Hw create a class vehicle and take the attributes from the parameter in the constructor and add the relevent methods to it
# Hw create 3 child classes(or sub class ) of animal class and create object of each child class(or sub class )
# write what did u understand and what's going on in this code in your own words in hindi