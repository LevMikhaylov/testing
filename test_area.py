import pytest
def calculate_area(length,width):
  return length*width
@pytest.mark.parametrize("length,width,expected",[(2,3,6),(4,5,20),(8,8,64),(5,6,3)])
def test_calculate_area(length,width,expected):
  assert calculate_area(length,width)==expected
