#Inheritance in OOP
class Animal :
    def __init__(self,name):
        self.name = name 

    def sound(self):
        return f"{self.name} makes a sound"


class Dog(Animal) : #child class that inherts the methods and attributes of the animal class 
    bark = "Woof!" #class attribute

    def sound(self):
        """returning the output of sound() method and add back the class variable later ,use the super() function"""
        base = super().sound()
        return f"{base},{self.name} barks {self.bark}" #overriding/replacing  the sound() method in the parent class in the child class to use the class attribute

class_object = Dog("Bingo")
print(class_object.sound())
            
#an order processing logic using multiple inheritance 
# --- Parent Class 1: The Core Base Class ---
class BaseOrderProcessor:
    """Handles the core business logic of an order."""
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def process(self):
        print(f"💰 Processing payment of ${self.amount} for Order #{self.order_id}.")


# --- Parent Class 2: A specialized Mixin for Logging ---
class LoggerMixin:
    """Provides automated system logging."""
    def process(self):
        print(f"📝 LOG: Initiating workflow for Order #{self.order_id}.")
        super().process()  # Passes control to the next class in line
        print(f"📝 LOG: Successfully completed workflow for Order #{self.order_id}.")


# --- Parent Class 3: A specialized Mixin for Notifications ---
class EmailNotifierMixin:
    """Provides automated email alerts."""
    def process(self):
        super().process()  # Passes control to the next class in line
        print(f"📧 EMAIL: Receipt sent to customer for Order #{self.order_id}.")


# --- Child Class: Combining everything using Multiple Inheritance ---
class DigitalOrderProcessor(LoggerMixin, EmailNotifierMixin, BaseOrderProcessor):
    """A specialized processor that logs events, processes payment, and emails a download link."""
    def process(self):
        print("🚀 Starting Digital Product Delivery Pipeline...")
        super().process()  # Triggers the chain of parent classes
        print("🔗 DOWNLOAD LINK: Sent product access keys.")

order_processor = DigitalOrderProcessor("98AO1",5000) 
order_processor.process()
    


