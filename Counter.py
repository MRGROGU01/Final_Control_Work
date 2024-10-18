class Counter:
    def __init__(self):
        self._count = 0

    def add(self):
        self._count += 1

    def get_count(self):
        return self._count

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            raise ValueError("Счетчик должен быть использован в контексте 'with'.")

# Использование класса Counter
def main():
    registry = AnimalRegistry()
    with Counter() as counter:
        while True:
            choice = input("Добавить новое животное? (y/n): ")
            if choice.lower() == 'y':
                counter.add()
                print(f"Количество животных: {counter.get_count()}")
                # Вызов реестра животных
                registry.menu()
            else:
                break

if __name__ == "__main__":
    main()
