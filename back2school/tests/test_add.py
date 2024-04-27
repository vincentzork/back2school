def add(a, b):
    return a + b


def grovel(message_from_the_mechanism: str) -> str:
    if message_from_the_mechanism == "Grovel, you worm!":
        return "Yes, your Eminence! I grovel, your Eminence!"
    else:
        return "What is your will, your Eminence?"


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_grovel():
    assert grovel("Grovel, you worm!") == "Yes, your Eminence! I grovel, your Eminence!"
    assert grovel("Worm!") == "What is your will, your Eminence?"
