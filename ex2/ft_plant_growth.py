#!/usr/bin/env python3

class  Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate = 0.8) -> None:
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
    def grow(self, days = 1) -> None:
        self.height += days * self.growth_rate
        self.age += days
    def show(self) -> None:
        init_height: float = self.height
        print('=== Garden Plant Growth ===')
        for i in range(1, 8):
            self.grow()
            print(
                f'=== Day {i} ===\n'
                f'{self.name.capitalize()}: '
                f'{self.height:.1f}cm, '
                f'{self.age} days old'
            )
        grown: float = self.height - init_height
        print(f'Growth this week: {grown:.1f}cm')


if __name__ == "__main__":
    def main() -> None:
        myPlant = Plant('Rose', 25, 30)
        myPlant.show()

main()
