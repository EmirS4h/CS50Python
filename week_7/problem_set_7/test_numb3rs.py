from numb3rs import validate


def test_bigger():
    assert validate("127.256.0.1") == False
    assert validate("255.255.255.310") == False
    assert validate("275.3.6.28") == False


def test_lower():
    assert validate("-100.36.0.1") == False
    assert validate("117.-6.2.0") == False
    assert validate("0.36.0.-6") == False


def test_in_range():
    assert validate("127.0.0.1") == True
    assert validate("255.0.255.1") == True
    assert validate("128.10.00.31") == True


def test_not_a_number():
    assert validate("cat") == False
    assert validate("dog") == False
    assert validate("meow") == False
