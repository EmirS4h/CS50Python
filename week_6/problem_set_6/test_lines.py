from lines import number_of_lines

def test_lines():
    assert number_of_lines("lines.py") == 25
    assert number_of_lines("pizza.py") == 19