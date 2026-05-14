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
        self._stats = Plant.Stats()

        self.set_height(height)
        self.set_age(age)
        self.set_growth_rate(growth_rate)

    class Stats():

        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def get_grow_calls(self) -> int:
            return self._grow_calls

        def count_grow_calls(self) -> None:
            self._grow_calls += 1

        def get_age_calls(self) -> int:
            return self._age_calls

        def count_age_calls(self) -> None:
            self._age_calls += 1

        def get_show_calls(self) -> int:
            return self._show_calls

        def count_show_calls(self) -> None:
            self._show_calls += 1

        def show_stats(self) -> None:
            print(
                    f"Stats: {self.get_grow_calls()} grow, "
                    f"{self.get_age_calls()} age, "
                    f"{self.get_show_calls()} show"
            )

    @classmethod
    def anonymous(cls: type["Plant"]) -> "Plant":
        anonymous_plant = cls(
                    name=f"Unknown {cls.__name__.lower()}",
                    height=Plant.DEFAULT_HEIGHT,
                    age=Plant.DEFAULT_AGE,
                    growth_rate=Plant.DEFAULT_GROWTH_RATE
        )
        return anonymous_plant

    @staticmethod
    def older_than_year(age: int) -> bool:
        return age > 365

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
        self._stats.count_grow_calls()

    def age(self, days: int) -> None:
        if days <= 0:
            print("Days must be positive")
            return
        self.set_age(self.get_age() + days)
        self._stats.count_age_calls()

    def show(self) -> None:
        print(
            f"{self.get_name()}: "
            f"{self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )
        self._stats.count_show_calls()


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str = "unknown",
            bloomed: bool = False,
            growth_rate: float = Plant.DEFAULT_GROWTH_RATE
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._bloomed = bloomed

    def get_color(self) -> str:
        return self._color

    def blooming(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color:{self.get_color()}")
        if self._bloomed is False:
            print(f" {self.get_name()} has not bloomed yet")
        else:
            print(f" {self.get_name()} is blooming beautifully!")


class Seed(Flower):
    DEFAULT_N_SEEDS: int = 0

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str = "unknown",
            bloomed: bool = False,
            n_seeds: int = DEFAULT_N_SEEDS,
            growth_rate: float = Plant.DEFAULT_GROWTH_RATE
    ) -> None:
        super().__init__(name, height, age, color, bloomed, growth_rate)
        self._n_seeds = n_seeds

    def get_n_seeds(self) -> int:
        return self._n_seeds

    def set_n_seeds(self, value: int) -> None:
        if value < 0:
            print("")
            return
        self._n_seeds = value

    def blooming(self, value: int = DEFAULT_N_SEEDS) -> None:
        super().blooming()
        self.set_n_seeds(value)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.get_n_seeds()}")


class Tree(Plant):

    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_calls: int = 0

        def get_produce_shade_calls(self) -> int:
            return self._produce_shade_calls

        def count_produce_shade_calls(self) -> None:
            self._produce_shade_calls += 1

        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self.get_produce_shade_calls()} shade")

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float = 0,
            growth_rate: float = Plant.DEFAULT_GROWTH_RATE
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._stats: Tree.TreeStats = Tree.TreeStats()

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        print(
                f"Tree {self.get_name()} now produces a shade of "
                f"{self.get_height():.1f}cm long and "
                f"{self.get_trunk_diameter():.1f}cm wide."
        )
        self._stats.count_produce_shade_calls()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.get_trunk_diameter():.1f}")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str = "unknown",
            nutritional_value: int = 0,
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
        super().grow(days)
        self.set_nutritional_value(self.get_nutritional_value() + days)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.get_harvest_season()}")
        print(f" Nutritional value: {self.get_nutritional_value()}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant._stats.show_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")
    print("\n=== Flower")
    my_flower = Flower("rose", 15, 10, "red", False)
    my_flower.show()
    display_stats(my_flower)
    print(f"[asking the {my_flower.get_name().lower()} to grow and bloom]")
    my_flower.grow(10)
    my_flower.blooming()
    my_flower.show()
    display_stats(my_flower)
    print("\n=== Tree")
    my_tree = Tree("oak", 200, 365, 5)
    my_tree.show()
    display_stats(my_tree)
    print(f"[asking the {my_tree.get_name().lower()} to produce shade]")
    my_tree.produce_shade()
    display_stats(my_tree)
    print("\n=== Seed")
    my_seed = Seed("sunflower", 80, 45, "yellow", False)
    my_seed.show()
    print(f"[make {my_seed.get_name().lower()} grow, age and bloom]")
    my_seed.grow(30)
    my_seed.age(20)
    my_seed.blooming(42)
    my_seed.show()
    display_stats(my_seed)
    print("\n=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    main()
