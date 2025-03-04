# write a code based on type of inheritance har ek ke baare me likho what you u have understood and you have to create the classses and the object for the same
"""single inheritance"""
class Bird:
    def __init__(self,name,color,beak):
        self.name = name
        self.color = color
        self.beak = beak

    def speak(self):
        print(f"{self.name} is speaking with its {self.beak}")

    def flying(self):
        print(f"{self.name} which has feather color {self.color} is flying")

class Parrot(Bird):
    def __init__(self, name, color, beak ,vocabulary,eye):
        super().__init__(name, color, beak)
        self.vocabulary = vocabulary
        self.eye = eye

    def talking(self):
        print(f"{self.name} is saying {self.vocabulary}")

    def eat(self):    
        print(f"{self.name} who has {self.eye} is eating chilli")

bird1= Parrot("bily","Green",'short beak',"Hello!","red eye")

bird1.talking()
bird1.eat()
print("\n")


"""Multiple Inheritance """    
class Father:
    def __init__(self,name,eye,height,age,skincolor):
        self.name = name
        self.eye = eye
        self.height =height        
        self.age = age        
        self.skincolor = skincolor        

    def work(self):
        print(f"{self.name} who is {self.age} old is working")

    def reading(self):
        print(f"{self.name} who has {self.eye} is reading")

dad = Father('Jake','blue','6 feet tall',51,"fair")

class Mother:
    def __init__(self,name,eye,height,age,skincolor):
        self.name = name
        self.eye = eye
        self.height =height        
        self.age = age        
        self.skincolor = skincolor        

    def cook(self):
        print(f'{self.name} is making food')

    def walk(self):
        print(f'{self.name} who is {self.height} is walking slow')

mom = Mother("Mary","green","5'5 feet tall",48,"light" )

class Child(Father,Mother):
    def __init__(self, name, eye, height, age, skincolor,hair,gender,weight):
        super().__init__(name, eye, height, age, skincolor)
        self.hair = hair
        self.gender = gender
        self.weight = weight

    def write(self):
        print(f'{self.name} is writing')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def excersice(self):
        print(f'{self.name} who is {self.gender} has {self.hair} doing workout to lose his weight from {self.weight} to 50kg')
        
kid = Child('John','green'," 6'1 feet tall", 18, 'light','golden','Male', '60')

"""Multilevel Inheritance-"""
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f'{self.name} is speaking ')

    def walk(self):
        print(f'{self.name} is walking')

    def run(self):
        print(f'{self.name} is running')

class Mammal(Animal):
    def __init__(self, name, fur_colour):
        super().__init__(name)
        self.fur = fur_colour

    def features(self):
        print(f'{self.name} is a mammal with fur colour {self.fur}')

class Dog(Mammal):
    def __init__(self, name, fur_colour,teeth,breed):
        super().__init__(name, fur_colour)
        self.teeth = teeth
        self.breed = breed
    
    def play(self):
        print(f'{self.name} is a {self.breed} and he is playing with his owner')

    
# doggy = Dog("bob",'golden','sharp teeth','Golden retriever')

# doggy.speak()
# doggy.play()
# doggy.features()

""" Hierarchical inheritance """

class Animal:

    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name} is walking')

    
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name)
        self.age = age
        self.breed = breed

    def bark(self):
        print(f'{self.name} is barking')

class Human(Animal):
    def __init__(self, name, age, height, eye_colour):
        super().__init__(name)
        self.age = age
        self.height = height
        self.eye = eye_colour

    def speak(self):
        print(f'{self.name} is speaking ')

    def run(self):
        print(f'{self.name} is running')

    def feature(self):
        print(f'{self.name} is {self.age} old and his height and eye colour is {self.height} and {self.eye}')

class Cow(Animal):
    def __init__(self, name,voice,weight):
        super().__init__(name)
        self.voice = voice
        self.weight = weight

    def sound(self):
        print(f'{self.name} is cow and he make sound {self.voice}')

    def detail(self):
        print(f'{self.name} is a cow who weighs {self.weight}')

doggy = Dog("Bily",7,"husky")
person = Human('Carl',29,'6 feet','green')
cows = Cow('Bill','MOO! MOO!','300 pounds')
print('\n')

doggy.walk()
print('\n')

person.walk()
print('\n')

cows.walk()
print('\n')

doggy.bark()
print('\n')

cows.detail()
print('\n')

cows.sound()