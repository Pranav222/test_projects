import pytest
from even_odd import even_odd

def test_even_odd():
    a = 4
    output = even_odd(a)
    assert output == "even"
