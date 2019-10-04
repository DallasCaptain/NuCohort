class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.health = 100

    def greet(self,target):
        print(self.name.capitalize(), 'says "Hi" to', target.name.capitalize())

class Ninja(Human):
    def __init__(self,name,age):
        super().__init__(name,age)
    def taunt(self, target):
        print(self.name,'Says "You can not handle my kunfu. HAAII-YAAAAH!" to',target.name.capitalize())

class Pirate(Human):
    def __init__(self,name,age,weapon):
        super().__init__(name,age)
        self.weapon = weapon
    def taunt(self,target):
        print(self.name.capitalize(),'Says "Ye Arrr not strong enough, Ye Scallywag!(spits on ground) to',target.name.capitalize())

class Zombie(Human):
    def __init__(self,name,age,eyecolor):
        super().__init__(name,age)
        self.eyecolor = eyecolor
    def taunt(self,target):
        print(self.name.capitalize(),'Says "I want to eat u rrrrrrrrrrr brainzzzz" to', target.name.capitalize())





