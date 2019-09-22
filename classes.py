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

class Animal():
    def __init__(self):
        print ("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print ("I am eating")

my_animal = Animal()
class Dog(Animal): #derived class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def eat(self):
        print("The dog is eating")
    def bark(self):
        print("WOOF!")
my_dog = Dog()
my_dog.who_am_i() #Can use it because it is inherited!
my_dog.eat()

class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " woof!"
class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " mewo!"

niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak()) #Same method name but different output
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
#abstract classes, is a base class for others to inherit
class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("subclass must implement this abstract method") # should modify in the in
        #inherited class!!
my_animal = Animal('fred')
#my_animal.speak()
class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"
class Cat(Animal):
    def speak(self):
        return self.name + " says meow"
fido = Dog("fido")
isis = Cat('isis')
print(isis.speak())
print(fido.speak())

#USe python methods on our classes
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self): #when a method asks for a string, returns thus
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted")
b = Book("Python", "Jose", 200)
print(b)
print(len(b))
del b #deletes variable from memory