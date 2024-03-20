class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed
    
    def sound(self):
        return 'Woof!'

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed
    
    def sound(self):
        return 'Meow!'

class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
    
    def sound(self):
        return 'Fox fox fox!'


if __name__ == '__main__':
    dog = Dog('Burek', 3, 'male', 'Labrador')
    cat = Cat('Mruczek', 2, 'female', 'Ragdoll')
    fox = Fox('Lis', 5, 'male')

    print(dog.name, dog.sound(), dog.breed)
    print(cat.name, cat.sound(), cat.breed)
    print(fox.name, fox.sound())
