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