# #In this lab, you'll build a game character stats tracker. 
# The program will allow you to create a character with specific attributes, 
# update those attributes, and retrieve the current stats of the character.

class GameCharacter : 
    def __init__(self,name):
        self._name = name 
        self._health = 100 
        self._mana = 50 
        self._level = 1 

    @property 
    def name(self) : 
        return self._name 

    @property 
    def health(self):
        return self._health

    @health.setter
    def health(self,health_score):
        if health_score < 0 : 
            self._health = 0 

        if health_score > 100 :
            self._health = 100 

        if 0 <= health_score <= 100: 
            self._health = health_score 

    @property 
    def mana(self): 
        return self._mana  

    @mana.setter 
    def mana(self,mana_score) :
        if mana_score < 0 :
            self._mana = 0

        if mana_score > 50 : 
            self._mana = 50 

        if 0 <= mana_score <= 50 : 
            self._mana = mana_score 


    @property
    def level(self):
        return self._level 

    def level_up(self):
        self._level += 1 
        self.health = 100
        self.mana = 50 

        print(f"{self.name} leveled up to {self._level}!")    

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Level: {self._level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}"
            )

hero = GameCharacter('Kratos')      
print(hero)      


