class Animal:
    def __init__(
            self, name: str,
            appetite: int,
            is_hungry: bool = True
                ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
                ) -> None:
        super().__init__(name, appetite=3)
        self.is_hungry = is_hungry

    def catch_mouse(self) -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7)
        self.is_hungry = is_hungry

    def bring_slippers(self) -> str:
        print("The slippers delivered!")


def feed_animals(list_animals: list) -> int:
    score = 0
    for class_animal in list_animals:
        score += class_animal.feed()
    return score
