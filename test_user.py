import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def user_data():
    return {
        "id": 1,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password",
        "phone": "123-456-7890",
        "userStatus": 0
    }

def test_create_user(user_data):
    response = requests.post(f"{BASE_URL}/user", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json()
    assert response_data.get("message") == "1", "Unexpected response message."

def test_get_user_by_username(user_data):
    # Создаем пользователя для получения
    requests.post(f"{BASE_URL}/user", json=user_data, headers=HEADERS)
    
    response = requests.get(f"{BASE_URL}/user/{user_data['username']}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json()
    
    assert response_data.get("username") == user_data["username"], "Username does not match."
    assert response_data.get("email") == user_data["email"], "Email does not match."

def test_update_user(user_data):
    # Создаем пользователя для обновления
    requests.post(f"{BASE_URL}/user", json=user_data, headers=HEADERS)
    
    # Обновляем данные пользователя
    user_data["firstName"] = "Updated"
    response = requests.put(f"{BASE_URL}/user/{user_data['username']}", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    # Проверяем обновленные данные
    response = requests.get(f"{BASE_URL}/user/{user_data['username']}")
    updated_data = response.json()
    assert updated_data.get("firstName") == "Updated", "First name did not update."

def test_delete_user(user_data):
    # Создаем пользователя для удаления
    requests.post(f"{BASE_URL}/user", json=user_data, headers=HEADERS)
    
    response = requests.delete(f"{BASE_URL}/user/{user_data['username']}")
    assert response.status_code == 200, f"Unexpected status code for DELETE request: {response.status_code}"
    
    # Проверка, что пользователь был удален
    response = requests.get(f"{BASE_URL}/user/{user_data['username']}")
    assert response.status_code == 404, f"Expected 404 for deleted user, got {response.status_code}"
