class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal():
    def __init__(self,name,age,health = 100,happiness = 100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness\
        
    def attr(self):
        return {
            'name':self.name,
            'age':self.age,
            'health':self.health,
            'happiness':self.happiness
        }
    def feed(self):
        self.health+=10
        self.happiness+=10
        return self

    def display_info(self):
        for key,val in self.attr().items():
            print(key,val)
        # print("Name:",self.name)
        # print("Health:",self.health)
        # print("Happiness",self.happiness)
        # print("Age",self.age)

        return self

class Chinchilla(Animal):
    def __init__(self,name,age,health=75,happiness=150):
        super().__init__(name,age,health,happiness)
        self.jumpHeight = 5
        self.softness = 9001
    def attr(self):
        super_attr = super().attr()
        super_attr['jumpHeight']=self.jumpHeight
        super_attr['softness'] = self.softness

        return super_attr
    def charm(self,target):
        boo = Chinchilla('boo',0)
        self.happiness += 3
        target.happiness += 3
        return boo

chinchillas = []
chinchillas.append(Chinchilla('pebbles',2,happiness=195))
chinchillas.append(Chinchilla('penelopy',2))
chinchillas.append(chinchillas[0].charm(chinchillas[1]))
chinchillas[2].name = 'leo'
for chin in chinchillas:
    chin.display_info()

# bob = Animal('bob',99,100000,3)

# print(bob.attr())
# bob.display_info()
# zoo1 = Zoo("John's Zoo")
# zoo1.add_lion("Nala")
# zoo1.add_lion("Simba")
# zoo1.add_tiger("Rajah")
# zoo1.add_tiger("Shere Khan")
# zoo1.print_all_info()