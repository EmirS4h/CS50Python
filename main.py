import sys
from week_0 import main as w0

def main():
    arguments = sys.argv
    if len(arguments) < 1:
        print("You didn't choose any chapter")
    
    match arguments[1]:
        case "week_0":
            w0()
        case _:
            print(f"Chapter with name '{arguments[1]}' does not exist!")


if __name__ == "__main__":
    main()