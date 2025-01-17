import pytest

@pytest.mark.parametrize("n, resultado", [(5, 15), (6, 48), (7, 105), (8, 384)])
def test_doble_factorial(n, resultado):
    assert doble_factorial(n) == resultado
