from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, breed, commands=None):
        self.name = name
        self.breed = breed
        self.commands = commands if commands else []

    @abstractmethod
    def make_sound(self):
        pass

    def add_command(self, command):
        self.commands.append(command)

class DomesticAnimal(Animal):
    def __init__(self, name, breed, commands=None):
        super().__init__(name, breed, commands)

    @abstractmethod
    def pet(self):
        pass

class PackAnimal(Animal):
    def __init__(self, name, breed, commands=None):
        super().__init__(name, breed, commands)

    @abstractmethod
    def pack(self):
        pass

class Dog(DomesticAnimal):
    def make_sound(self):
        return "Woof!"

    def pet(self):
        return "Wagging tail"

class Cat(DomesticAnimal):
    def make_sound(self):
        return "Meow!"

    def pet(self):
        return "Purring"

class Hamster(DomesticAnimal):
    def make_sound(self):
        return "Squeak!"

    def pet(self):
        return "Running in wheel"

class Horse(PackAnimal):
    def make_sound(self):
        return "Neigh!"

    def pack(self):
        return "Carrying load"

class Donkey(PackAnimal):
    def make_sound(self):
        return "Hee-haw!"

    def pack(self):
        return "Carrying load"

class Counter:
    def __init__(self):
        self.count = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            raise Exception("Counter resource was not closed properly")

    def add(self):
        self.count += 1

def add_animal(registry):
    name = input("Enter animal name: ")
    breed = input("Enter animal breed: ")
    animal_type = input("Enter animal type (dog, cat, hamster, horse, donkey): ")

    if animal_type == "dog":
        animal = Dog(name, breed)
    elif animal_type == "cat":
        animal = Cat(name, breed)
    elif animal_type == "hamster":
        animal = Hamster(name, breed)
    elif animal_type == "horse":
        animal = Horse(name, breed)
    elif animal_type == "donkey":
        animal = Donkey(name, breed)
    else:
        print("Invalid animal type")
        return

    registry.append(animal)
    print(f"{animal_type.capitalize()} {name} added to the registry")

def list_commands(registry):
    name = input("Enter animal name: ")
    for animal in registry:
        if animal.name == name:
            print(f"Commands for {animal.name}: {', '.join(animal.commands)}")
            return
    print("Animal not found in the registry")

def train_animal(registry):
    name = input("Enter animal name: ")
    command = input("Enter new command: ")
    for animal in registry:
        if animal.name == name:
            animal.add_command(command)
            print(f"{animal.name} learned new command: {command}")
            return
    print("Animal not found in the registry")

def main():
    registry = []
    counter = Counter()

    while True:
        print("\nAnimal Registry Menu:")
        print("1. Add new animal")
        print("2. List commands")
        print("3. Train animal")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                with counter:
                    add_animal(registry)
                    counter.add()
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            list_commands(registry)
        elif choice == "3":
            train_animal(registry)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
