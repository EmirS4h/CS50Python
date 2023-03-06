from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("Twitter") == "Twttr"
    assert shorten("emirsahin") == "mrshn"
