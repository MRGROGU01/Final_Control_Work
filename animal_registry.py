class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_commands(self):
        for animal in self.animals:
            print(f"{animal}: Команды - {animal.get_commands()}")

    def menu(self):
        while True:
            print("\nМеню:")
            print("1. Завести новое животное")
            print("2. Показать команды всех животных")
            print("3. Выход")
            choice = input("Выберите опцию: ")

            if choice == '1':
                name = input("Введите имя животного: ")
                birth_date = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
                animal_type = input("Введите тип животного (собака/кошка/лошадь/осел): ").lower()

                if animal_type == 'собака':
                    animal = Dog(name, birth_date)
                elif animal_type == 'кошка':
                    animal = Cat(name, birth_date)
                elif animal_type == 'лошадь':
                    animal = Horse(name, birth_date)
                elif animal_type == 'осел':
                    animal = Donkey(name, birth_date)
                else:
                    print("Неизвестный тип животного.")
                    continue

                commands = input("Введите команды, разделенные запятой: ").split(',')
                for command in commands:
                    animal.add_command(command.strip())

                self.add_animal(animal)

            elif choice == '2':
                self.display_commands()

            elif choice == '3':
                print("Выход из программы.")
                break

            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
