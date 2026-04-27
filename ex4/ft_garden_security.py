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
            growth_rate: float = DEFAULT_GROWTH_RATE
    ) -> None:
        self._name = name
        self._height = Plant.DEFAULT_HEIGHT
        self._age = Plant.DEFAULT_AGE

        self.set_height(height)
        self.set_age(age)
        self.set_growth_rate(growth_rate)

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value < 0.0:
            print('Height must be positive')
            return
        else:
            self._height = value

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            print('Age cannot be negative')
            return
        else:
            self._age = value

    def get_growth_rate(self) -> float:
        return self._growth_rate

    def set_growth_rate(self, value: float) -> None:
        if value <= 0:
            print('Growth rate must be positive')
            return
        else:
            self._growth_rate = value

    def grow(self, days: int = 7) -> None:
        if days <= 0:
            print('Days must be positive')
            return
        init_height: float = self.get_height()
        print('=== Garden Plant Growth ===')
        for i in range(1, days + 1):
            self.set_height(self.get_height() + self.get_growth_rate())
            self.set_age(self.get_age() + 1)
            print(
                f'=== Day {i} ===\n'
                f'{self._name.capitalize()}: '
                f'{self.get_height():.1f}cm, '
                f'{self.get_age()} days old'
            )
        grown: float = self.get_height() - init_height
        print(f'Growth this week: {grown:.1f}cm\n')

    def show(self) -> None:
        print(
                f'{self._name.capitalize()}: '
                f'{self.get_height():.1f}cm, '
                f'{self.get_age()} days old'
        )


def main() -> None:
    plants = [
            Plant('rose', 25, 30),
            Plant('oak', 200, 365),
            Plant('cactus', 5, 90),
            Plant('sunflower', 80, 45),
            Plant('fern', 15, 120)
    ]
    for plant in plants:
        print('Created: ', end='')
        plant.grow()
        plant.show()


if __name__ == "__main__":
    main()
