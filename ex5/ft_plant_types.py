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

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value < 0.0:
            print(
                    f"{self.get_name()}: Error, height can't be negative\n"
                    "Height update rejected"
            )
            return
        else:
            self._height = value

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            print(
                    f"{self.get_name()}: Error, age can't be negative\n"
                    "Age update rejected"
            )
            return
        else:
            self._age = value

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
                f"{self.get_name()}: "
                f"{self.get_height():.1f}cm, "
                f"{self.get_age()} days old"
            )
        grown: float = self.get_height() - init_height
        print(f"Growth this week: {grown:.1f}cm\n")

    def show(self) -> None:
        print(
            f"{self.get_name()}: "
            f"{self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str,
            bloomed: bool,
            growth_rate: float = Plant.DEFAULT_GROWTH_RATE
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._bloomed = False

    def get_color(self) -> str:
        return self._color

    def blooming(self) -> None:
        if self._bloomed is False:
            print(
                    f"i {self.get_name()} has not bloomed yet\n"
                    f"[asking the {self.get_name().lower()} to bloom]"
            )
            self._bloomed = True
        else:
            print(f" {self.get_name()} is blooming beautifully!]")
            self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color:{self.get_color()}")
        self.blooming()


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float,
            growth_rate: float = Plant.DEFAULT_GROWTH_RATE
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        print(
                f"[asking the {self.get_name()} to produce shade]\n"
                f"Tree {self.get_name()} now produces a shade of "
                f"{self.get_height():.1f}cm long and "
                f"{self.get_trunk_diameter():.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter:{self.get_trunk_diameter():.1f}")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: int,
            growth_rate: float = Plant.DEFAULT_GROWTH_RATE
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = nutritional_value

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def set_nutritional_value(self, value: int) -> None:
        if value <= 0:
            print("Nutritional value must be positive")
            return
        else:
            self._nutritional_value = value

    def grow(self, days: int) -> None:
        self.set_age(self.get_age() + days)
        self.set_nutritional_value(self.get_nutritional_value() + days)
        print(
                f"[make {self.get_name().lower()} "
                f"grow and age for {days} days]"
        )

    def show(self) -> None:
        super().show()
        print(f" Harvest season:{self.get_harvest_season()}")
        print(f" Nutritional value:{self.get_nutritional_value()}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    my_flower = Flower("rose", 15, 10, "red", False)
    my_flower.show()
    my_flower.show()
    print("\n=== Tree")
    my_tree = Tree("oak", 200, 365, 5)
    my_tree.show()
    my_tree.produce_shade()
    print("\n=== Vegetable")
    my_vegetable = Vegetable("tomato", 5, 10, "april", 0, 2.1)
    my_vegetable.show()
    my_vegetable.grow(20)
    my_vegetable.show()


if __name__ == "__main__":
    main()
