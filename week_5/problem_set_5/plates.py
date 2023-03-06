def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate: str) -> bool:
    if 1 < len(plate) <= 6 and plate[:2].isalpha() and plate.isalnum():
        slc = [plate[:len(plate)//2], plate[len(plate)//2:]]
        if slc[1][0] == '0':
            return False
        else:
            return True
    return False


if __name__ == "__name__":
    main()
