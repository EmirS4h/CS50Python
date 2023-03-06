from bank import value

def test_h():
    assert value("h") == 20
    assert value("H") == 20

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HeLlO") == 0

def test_other():
    assert value("sup") == 100
    assert value("nice") == 100