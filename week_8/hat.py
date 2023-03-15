from random import choice


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name: str):
        print(f"{name} is in {choice(cls.houses)}")


def main():
    Hat.sort("Harry")


if __name__ == "__main__":
    main()
