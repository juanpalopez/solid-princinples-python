import os
from src.liskov_substitution_principles import rectangle
print(os.getcwd())


def test_rectangle_area():
    testHeight = 2
    testWidth = 2
    expectedArea = 4
    rectan = rectangle.Rectangle(testWidth, testHeight)
    assert expectedArea == rectan.get_area()
