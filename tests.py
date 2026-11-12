import pytest
from main import name_fix

@pytest.mark.parametrize("name, expected", [
    ("dR. JoHn SmiTH, Md", "John Smith"),
    ("jACqUeLINE jORdaN", "Jacqueline Jordan"),
    ("DR. LaUreN ClaRk DDs","Lauren Clark"),
    ("   robiN   coX   ","Robin Cox"),
    ("ms. Jane Doe","Jane Doe"),
    ("", ""),
])
def test_name_fix(name, expected):
    assert name_fix(name) == expected