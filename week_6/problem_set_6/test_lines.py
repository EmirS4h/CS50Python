from lines import number_of_lines


def test_lines():
    assert number_of_lines("lines.py") == 24
    assert number_of_lines("pizza.py") == 19
    assert number_of_lines("scourgify.py") == 37
