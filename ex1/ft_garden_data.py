#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
                f'{self.name.capitalize()}: '
                f'{self.height}cm, '
                f'{self.age} days old'
        )


if __name__ == "__main__":
    def main() -> None:
        plant1 = Plant('Rose', 25, 30)
        plant1.show()
        plant2 = Plant('sunflower', 80, 45)
        plant2.show()
        plant3 = Plant('cactus', 15, 120)
        plant3.show()

main()
