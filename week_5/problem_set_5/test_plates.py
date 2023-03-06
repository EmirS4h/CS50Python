from plates import is_valid


def test_numbers_in_middle():
    assert is_valid("CS50P") == True
    assert is_valid("MyPlate245Kek") == False


def test_starts_with_zero():
    assert is_valid("CS05") == False
    assert is_valid("MyPLate023") == False


def test_non_chars():
    assert is_valid("PI3.14") == False
