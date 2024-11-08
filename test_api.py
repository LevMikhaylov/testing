import requests
import pprint


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        # set headers, authorisation etc

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST':
                response = requests.post(url, data=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        # log part
        pprint.pprint(f'{request_type} example')
        pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        pprint.pprint(response.reason)
        pprint.pprint(response.text)
        pprint.pprint(response.json())
        pprint.pprint('**********')
        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body)
        return response.json()['message']

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()['message']


BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)
print("User API Requests")

# 1. GET пользователя
#print("GET User:")
#user_info = base_request.get('user', 'test_user', expected_error=True)  # Пользователь не существует
#pprint.pprint(user_info)

# 2. POST создать пользователя
print("POST User:")
new_user = {
    "id": 1234,
    "username": "test_user",
    "firstName": "Test",
    "lastName": "User",
    "email": "test_user@example.com",
    "password": "test_password",
    "phone": "123-456-7890",
    "userStatus": 1
}
created_user_response = base_request.post('user', 1, new_user)
pprint.pprint(created_user_response)

# 3. GET созданного пользователя
print("GET Created User:")
created_user_info = base_request.get('user', 'test_user')
pprint.pprint(created_user_info)
assert new_user["id"]== created_user_info["id"]
pass

# 4. DELETE пользователя
print("DELETE User:")
delete_user_response = base_request.delete('user', 'test_user')
pprint.pprint(delete_user_response)

# Проверяем, что пользователь удален
print("GET Deleted User:")
deleted_user_info = base_request.get('user', 'test_user', expected_error=True)
pprint.pprint(deleted_user_info)

# Примеры запросов для сущности store
print("\nStore API Requests")

# 1. GET inventory
print("GET Inventory:")
inventory_info = base_request.get('store', 'inventory')
pprint.pprint(inventory_info)

# 2. POST создать заказ
print("POST Order:")
new_order = {
    "id": 12345,
    "petId": 1,
    "quantity": 2,
    "shipDate": "2021-11-01T00:00:00.000Z",
    "status": "placed",
    "complete": True
}
created_order_response = base_request.post('store/order', 1, new_order)
pprint.pprint(created_order_response)

# 3. GET созданного заказа
print("GET Created Order:")
created_order_info = base_request.get('store/order', created_order_response['id'])
pprint.pprint(created_order_info)
assert new_order["id"]==created_order_info["id"]
pass

# 4. DELETE заказ
print("DELETE Order:")
delete_order_response = base_request.delete('store/order', created_order_response['id'])
pprint.pprint(delete_order_response)

# Проверяем, что заказ удален
print("GET Deleted Order:")
deleted_order_info = base_request.get('store/order', created_order_response['id'], expected_error=True)
pprint.pprint(deleted_order_info)
