class Wizard:
    def __init__(self, name: str) -> None:
        self.name = name


class Student(Wizard):
    def __init__(self, name: str, house: str) -> None:
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albas")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
