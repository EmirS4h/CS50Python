import sys
from week_0.main import run_week_0_functions_and_variables


def main():
    arguments = sys.argv
    if len(arguments) < 2:
        sys.exit("You didn't choose any week")
    match arguments[1]:
        case "week_0":
            run_week_0_functions_and_variables()
        case _:
            sys.exit(f"Week with name '{arguments[1]}' does not exist!")


if __name__ == "__main__":
    main()
