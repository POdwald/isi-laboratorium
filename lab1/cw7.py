class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def sound(self):
        output = f'{self.name} is barking!'
        print(output)


if __name__ == '__main__':
    uroczy_piesek = Dog('Burek', 2, 'Red')
    glosny_piesek = Dog('Reksio', 3, 'Brown')
    przeslodki_piesek = Dog('Pimpek', 4, 'Black')

    uroczy_piesek.sound()
    glosny_piesek.sound()
    przeslodki_piesek.sound()