import pytest
def is_even(number):
  return number % 2 == 0
@pytest.mark.parametrize("number,expected",[(2,True),(3,False),(4,True),(5,False)])
def test_is_even(number,expected):
  assert is_even(number) == expected
