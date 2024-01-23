def fibonacci import calc_fibo
import pytest

@pytest.mark.parameytize("n,result", [
    (5, 8)
    (1, 1)
    (4, 5)
    (7, 21),
])
def test_fibonacci(n, result):
    assert calc_fibo(5) == result

