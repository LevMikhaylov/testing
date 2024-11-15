import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def store_data():
    return {
        "id":1,
        "petId":1,
        "quantity":2,
        "shipDate":"2024-11-15T12:36:19.606Z",
        "status":"placed",
        "complete":True
    }

def test_post_create_order(store_data):
    response = requests.post(f"{BASE_URL}/store/order", json=store_data, headers=HEADERS)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("id") == store_data["id"], "Store ID does not match."

def test_get_order_by_id(store_data):
    store_id = store_data["id"]
    response = requests.get(f"{BASE_URL}/store/order/{store_id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("id") == store_id, "Store ID does not match in GET request."
    assert response_data.get("petId") == store_data["petId"], "Store petID does not match in GET request."

def test_get_order_by_status(store_data):
    create_response = requests.post(f"{BASE_URL}/store/order", json=store_data, headers=HEADERS)
    assert create_response.status_code == 200, f"Failed to create order: {create_response.status_code}"
    created_order = create_response.json()
    assert created_order.get("status") == store_data["status"], "The status of the created order does not match."
    response = requests.get(f"{BASE_URL}/store/order/{created_order['id']}")
    assert response.status_code == 200, f"Unexpected status code while checking order: {response.status_code}"
    order_data = response.json()
    assert order_data.get("status") == store_data["status"], "The returned order status does not match."


def test_delete_order(store_data):
    store_id = store_data["id"]
    response = requests.delete(f"{BASE_URL}/store/order/{store_id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code} for DELETE request"

    # Проверка, что питомец был удален
    response = requests.get(f"{BASE_URL}/strore/order/{store_id}")
    assert response.status_code == 404, f"Expected 404 for deleted pet, got {response.status_code}"
