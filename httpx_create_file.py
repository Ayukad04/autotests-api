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


create_file_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data={"filename": "python_image.jpg", "directory": "courses"},
    files={"upload_file": open('./testdata/files/python.png', 'rb')},
    headers=create_file_headers
)

create_file_response_data = create_file_response.json()
print('Create file data:', create_file_response_data)