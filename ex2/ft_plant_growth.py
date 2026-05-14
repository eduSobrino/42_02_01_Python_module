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
        if value <= 0:
            print("Height must be positive")
            return
        self._height = value

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            print("Age cannot be negative")
            return
        self._age = value

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
    my_plant = Plant("Rose", 25, 30)
    grown: float = 0
    steps: int = 1
    print("=== Garden Plant Growth ===")
    my_plant.show()
    for i in range(1, 8, steps):
        my_plant.grow(i)
        grown += my_plant.get_growth_rate()
        my_plant.age(i)
        print(f"=== Day {i} ===")
        my_plant.show()
    print(f"Growth this week: {grown:.1f}cm")


if __name__ == "__main__":
    main()
