class Student():
    def __init__(self, name: str, house: str):
        self.name = name
        self.house = house

    def __str__(self):
        return f"Student {self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Slytherin", "Gryffindor", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name, house = input("Name and House: ").split(",")
        return cls(name.strip(), house.strip())


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
