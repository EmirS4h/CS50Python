import random


def main():
    score: int = 0
    questions: list[str] = []
    level: int = get_level()
    current_question_index: int = 0
    wrong_answer_count = 0

    # Generate question
    for _ in range(10):
        questions.append(
            f"{generate_integer(level)} + {generate_integer(level)}")

    while True:
        try:
            # Check if there are more questions
            if current_question_index < len(questions):
                # get the numbers
                x, y = questions[current_question_index].split("+")
                # get the answer
                answer = int(input(f"{x.strip()} + {y.strip()} = "))
                # check if answer is correct
                if answer == int(x) + int(y):
                    current_question_index += 1
                    score += 1
                    wrong_answer_count = 0
                else:
                    wrong_answer_count += 1
                    if wrong_answer_count == 3:
                        wrong_answer_count = 0
                        current_question_index += 1
                        print(
                            f"Correct answer is {x.strip()} + {y.strip()} = {int(x)+int(y)}")
                    continue
            else:
                print(f"Your score is : {score}")
                break
        except ValueError:
            pass
        except EOFError:
            break
        except KeyboardInterrupt:
            break


def get_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                return level
            continue
        except ValueError:
            pass


def generate_integer(digits: int) -> int:
    if digits > 0 and digits < 4:
        return random.randint(10**(digits-1), (10**digits)-1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
