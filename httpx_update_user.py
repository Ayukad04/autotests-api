import httpx

from tools.fakes import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "qwer123",
    "lastName": "Иванов",
    "firstName": "Иван",
    "middleName": "Иванович"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(create_user_response.status_code)
print(create_user_response_data)

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

patch_user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

patch_user_payload = {
    "lastName": "Семёнов",
    "firstName": "Сергей",
    "middleName": "Александрович"
}

patch_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
                                 headers=patch_user_headers, json=patch_user_payload)

patch_user_response_data = patch_user_response.json()
print(patch_user_response.status_code)
print(patch_user_response_data)

