import pytest
def string_len(s):
  return len(s)

@pytest.mark.parametrize("s,expected",[("",0),("   ",3),("Это\nмногострочная\nстрока",24)])
def test_string_length(s,expected):
  assert string_len(s)==expected
