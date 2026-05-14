#!/usr/bin/env python3


class Plant:
    DEFAULT_GROWTH_RATE = 0.8

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = DEFAULT_GROWTH_RATE
    ) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value < 0.0:
            print(
                    f"{self._name}: Error, height can't be negative\n"
                    "Height update rejected"
            )
            return
        self._height = value
        print(f"Height updated: {self.get_height()} days")

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            print(
                    f"{self._name}: Error, age can't be negative\n"
                    "Age update rejected"
            )
            return
        self._age = value
        print(f"Age updated: {self.get_age()} days")

    def get_growth_rate(self) -> float:
        return self._growth_rate

    def set_growth_rate(self, value: float) -> None:
        if value <= 0:
            print("Growth rate must be positive")
            return
        self._growth_rate = value

    def grow(self, days: int) -> None:
        if days <= 0:
            print("Days must be positive")
            return
        self.set_height(self.get_height() + days * self.get_growth_rate())

    def age(self, days: int) -> None:
        if days <= 0:
            print("Days must be positive")
            return
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        print(
                f"{self.get_name()}: "
                f"{self.get_height():.1f}cm, "
                f"{self.get_age()} days old"
        )


def main() -> None:
    print("=== Plant Security System ===")
    my_plant = Plant("rose", 15, 10)
    print("Created: ", end="")
    my_plant.show()
    print("\n")
    my_plant.set_height(25)
    my_plant.set_age(30)
    print("\n")
    my_plant.set_height(-12)
    my_plant.set_age(-9)
    print("\nCurrent state: ", end="")
    my_plant.show()


if __name__ == "__main__":
    main()
