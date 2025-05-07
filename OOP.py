
class Animals:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
# dont forget that __init__ double underscore (dunder methods(magic methods)) makes print and there are other dunder methods
# like __str__ , __eq__, __gt__
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")



#Inheritance
class Dog(Animals):
    pass
class Cat(Animals):
    pass
class Mouse(Animals):
    pass

dog = Dog("Scooby")
dog2 = Dog("Odin")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)

dog2.eat()


