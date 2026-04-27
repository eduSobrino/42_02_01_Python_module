#!/usr/bin/env python3

class Plant:

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth_rate: float = 0.8
    ) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if value <= 0:
            raise ValueError('Height must be positive')
        self._height = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError('Age cannot be negative')
        self._age = value

    @property
    def growth_rate(self) -> float:
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float) -> None:
        if value <= 0:
            raise ValueError('Growth rate must be positive')
        self._growth_rate = value

    def grow(self, days: int = 7) -> None:
        if days <= 0:
            raise ValueError('Days must be positive')
        init_height: float = self.height
        print('=== Garden Plant Growth ===')
        for i in range(1, days + 1):
            self.height += self.growth_rate
            self.age += 1
            print(
                f'=== Day {i} ===\n'
                f'{self.name.capitalize()}: '
                f'{self.height:.1f}cm, '
                f'{self.age} days old'
            )
        grown: float = self.height - init_height
        print(f'Growth this week: {grown:.1f}cm\n')

    def show(self) -> None:
        print(
                f'{self.name.capitalize()}: '
                f'{self.height:.1f}cm, '
                f'{self.age} days old'
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
        plant.show()


if __name__ == "__main__":
    main()
