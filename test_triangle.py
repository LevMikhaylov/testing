import pytest
def classify_triangle(a, b, c):
  if a < b+c and b < a+c and c < a+b:
    if (a==b and b!=c) or (a == c and c != b) or (b==c and c!=a):
      return "равнобедренный"
    elif a==b==c:
      return "равносторонний"
    else:
      return "разносторонний"
  else:
    return "это не треугольник"
@pytest.mark.parametrize("a,b,c,expected",[(3,3,3,"равносторонний"),
                                           (3,3,2,"равнобедренный"),
                                           (4,3,3,"равнобедренный"),
                                           (3,2,3,"равнобедренный"),
                                           (3,4,5,"разносторонний"),
                                           (1,2,3,"это не треугольник")])
def test_classify_triangle(a,b,c,expected):
  assert classify_triangle(a,b,c)==expected
