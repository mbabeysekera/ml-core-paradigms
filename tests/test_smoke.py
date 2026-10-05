from ml_core_paradigms.sample import greet


def test_greet():
    assert greet("World") == "Hello, World!"
