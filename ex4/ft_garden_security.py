#!/usr/bin/env python3


class Plant:
    DEFAULT_HEIGHT: float = 0.0
    DEFAULT_AGE: int = 0
    DEFAULT_GROWTH_RATE: float = 0.8

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = DEFAULT_GROWTH_RATE,
    ) -> None:
        self._name = name.capitalize()
        self._height = Plant.DEFAULT_HEIGHT
        self._age = Plant.DEFAULT_AGE

        self.set_height(height)
        self.set_age(age)
        self.set_growth_rate(growth_rate)

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value < 0.0:
            print(
                    f"{self._name}: Error, height can't be negative\n"
                    "Height update rejected"
            )
            return
        else:
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
        else:
            self._age = value
            print(f"Age updated: {self.get_age()} days")

    def get_growth_rate(self) -> float:
        return self._growth_rate

    def set_growth_rate(self, value: float) -> None:
        if value <= 0:
            print("Growth rate must be positive")
            return
        else:
            self._growth_rate = value

    def grow(self, days: int = 7) -> None:
        if days <= 0:
            print("Days must be positive")
            return
        init_height: float = self.get_height()
        print("=== Garden Plant Growth ===")
        for i in range(1, days + 1):
            self.set_height(self.get_height() + self.get_growth_rate())
            self.set_age(self.get_age() + 1)
            print(
                f"=== Day {i} ===\n"
                f"{self._name.capitalize()}: "
                f"{self.get_height():.1f}cm, "
                f"{self.get_age()} days old"
            )
        grown: float = self.get_height() - init_height
        print(f"Growth this week: {grown:.1f}cm\n")

    def show(self) -> None:
        print(
            f"{self._name}: "
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
    print("\n")
    print("Current state: ", end="")
    my_plant.show()


if __name__ == "__main__":
    main()
