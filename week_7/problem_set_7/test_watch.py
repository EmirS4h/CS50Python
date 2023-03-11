from watch import parse


def test_iframe():
    assert parse(
        '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'


def test_valid():
    assert parse(
        "http://youtube.com/embed/xvFZjo5PgG0") == 'https://youtu.be/xvFZjo5PgG0'
    assert parse(
        "https://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"
    assert parse(
        "https://www.youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"
    assert parse(
        "https://www.youtube.com/embed/UbxUSsFXYo4?modestbranding=0&amp;rel=0&amp;showinfo=0") == "https://youtu.be/UbxUSsFXYo4"


def test_invalid():
    assert parse(
        "http://youtube.com/xvFZjo5PgG0") == None
    assert parse(
        "https://www.youtube.com/embde/xvFZjo5PgG0") == None
