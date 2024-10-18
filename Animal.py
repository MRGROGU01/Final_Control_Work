class Animal:
    def __init__(self, name, birth_date):
        self._name = name  # Инкапсуляция
        self._birth_date = birth_date
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def get_commands(self):
        return self._commands

    def __str__(self):
        return f"{self._name}, дата рождения: {self._birth_date}"

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class DraftAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Dog(DomesticAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Cat(DomesticAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Horse(DraftAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Donkey(DraftAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
