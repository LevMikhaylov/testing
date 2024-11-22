import pytest
@pytest.fixture
def file_path():
  return "\\content\\"
def save_string_to_file(s:str,filename:str):
  with open(filename,"w") as file:
    file.write(s)
def test_save_to_file(file_path):
  test_string = "This is a test string"
  path = f"{file_path}test_file.txt"
  save_string_to_file(test_string,path)
  with open(path,"r") as file:
    content = file.read()
    assert content==test_string,"Содержимое файла не совпадает с ожидаемой строкой"
