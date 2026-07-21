# python abstraction in oop

import math 
from abc import ABC , abstractmethod 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width 

    def perimeter(self):
        return 2*(self.length + self.width)



class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)  

    def perimeter(self):
        return round(2*math.pi*self.radius, 2)    

shapes = [Rectangle(7,5), Circle(7)]
for shape in shapes :
    print(f'{shape.area()} square meters')
    print(f'{shape.perimeter()} meters')
