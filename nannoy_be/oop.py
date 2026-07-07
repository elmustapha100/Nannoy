class Cat: 
    def __init__(self,name,breed,diet):
        self.name = name
        self.breed = breed 
        self.diet = diet

    def sound(self):
        print(f"{self.name} is a {self.breed} type who is an obligate {self.diet} meows!")

#creating an object from the Cat class
cat = Cat("Nani","Siamese","carnivore")

#calling the sound method 
cat.sound()

class Dog: 
    def __init__(self,name):
        self.name = name 

    def bark(self):
        print(f"{self.name} says woof!")

dog = Dog('Rex')
print(dog.name)

 
