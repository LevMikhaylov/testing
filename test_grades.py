import pandas as pd
import pytest

def load_from_csv(file_path):
  ds = pd.read_csv(file_path)
  ds.columns = ds.columns.str.strip().str.replace('"', '')
  for column in ['Test1', 'Test2', 'Test3', 'Test4', 'Final']:
    ds[column] = pd.to_numeric(ds[column], errors='coerce')
  return ds

def calculate_average_grade(file_path):
  df = load_from_csv(file_path)
  df['Average'] = df[['Test1', 'Test2', 'Test3', 'Test4']].mean(axis=1)
  return df

@pytest.fixture
def file_path():
  return "grades.csv"

@pytest.mark.parametrize("test_input", ["grades.csv"])
def test_average_grade(test_input):
  ds1 = calculate_average_grade(test_input)
  assert ds1['Average'].equals(ds1['Final'])
