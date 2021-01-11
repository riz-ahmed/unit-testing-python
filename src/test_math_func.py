import math_func
import pytest

def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_product():
    assert math_func.product(2) == 4

def test_add_strings():
    result = math_func.add("Hello ", "World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Hwllod" not in result
