import os
import pytest
from src.liskov_substitution_principles import square
print(os.getcwd())


@pytest.mark.skip(reason="This test won't pass, violates LSP")
def test_square_area():
    ''' This test won't pass
    '''
    testHeight = 2
    testWidth = 4
    expectedArea = 8
    sqr = square.Square(testHeight)
    sqr.width = testWidth
    assert expectedArea == sqr.get_area()
