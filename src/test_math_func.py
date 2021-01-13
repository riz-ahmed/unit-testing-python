import math_func
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (4,0), reason="This test wil be skipped")                                     # using decorator function from pytest library
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

@pytest.mark.number
def test_product():
    assert math_func.product(2) == 4

@pytest.mark.strings                                    # using decorator fucntion from pytest for strings
def test_add_strings():
    result = math_func.add("Hello ", "World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Hwllod" not in result
