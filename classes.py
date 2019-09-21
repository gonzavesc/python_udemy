class Sample():
    pass
my_sample = Sample()
print(type(my_sample))

class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed = 'Lab', name ='Lara', spots = False)
print(my_dog.breed)

class Dog():
    #CLASS OBJECT ATTRIBUTE
    #SAME for instance of class
    species = 'mammal'
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    #OPERATIONS/CLASS --> metohd
    def bark(self):
        print("woof my name is {}".format(self.name))


my_dog = Dog(breed = 'Lab', name ='Lara', spots = False)
print(my_dog.species) #no need for ()
my_dog.bark()

class Circle():
    pi = 3.14159267
    def __init__(self, radius=1):
        self.radius = radius
    def get_circumference(self):
        return self.radius * Circle.pi * 2 #Class object atribute can be called like this
my_circle = Circle(10)
print(my_circle.get_circumference())