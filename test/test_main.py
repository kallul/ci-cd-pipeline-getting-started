from src.main import add

def test_add_function():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 1
    assert add(-5, -5) == -10

