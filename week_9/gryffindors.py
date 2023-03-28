def main():
    # students = [
    #     {"name": "Hermione", "house": "Gryffindor"},
    #     {"name": "Harry", "house": "Gryffindor"},
    #     {"name": "Ron", "house": "Gryffindor"},
    #     {"name": "Draco", "house": "Slytherin"},
    #     {"name": "Padma", "house": "Ravenclaw"},
    # ]
    # gryffindors = [
    #     student["name"] for student in students if student["house"] == "Gryffindor"
    # ]
    # print(*gryffindors)

    # gryffindors = filter(is_gryffindor, students)

    # for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
    #     print(gryffindor["name"])

    # d = {str(i): i*2 for i in range(1, 10, 2)}
    # print(d)

    students = ["Hermione", "Harry", "Ron"]
    # gryffindors = []
    # for student in students:
    #     gryffindors.append({"name":student,"house":"Gryffindor"})
    # print(gryffindors)

    # gryffindors = [{"name": student, "house": "Gryffindor"}
    #                for student in students]
    # gryffindors = {student: "Gryffindor" for student in students}
    # gryffindors = {"Gryffindor": [student for student in students]}
    # print(gryffindors)

    for index, student in enumerate(students, start=1):
        print(index, student)


def is_gryffindor(student):
    return student["house"] == "Gryffindor"


if __name__ == "__main__":
    main()
