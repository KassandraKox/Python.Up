# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


class Fish(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Мелководная", "Глубоководная")[self.feature > 1000]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nГлубина: {self.feature}\nТип: {self.type}\n'


class Bird(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Хищная", "Домашняя")[self.feature > 3]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nВид: {self.feature}\nТип: {self.type}\n'


class Mammals(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Мелкий", "Крупный")[self.feature > 100]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nВес: {self.feature}\nТип: {self.type}\n'


if __name__ == '__main__':
    f = Fish('Dori', 1, 40)
    b = Bird('Govorun', 2, 2)
    m = Mammals('Kenga', 8, 85)

    print(f)
    print(b)
    print(m)