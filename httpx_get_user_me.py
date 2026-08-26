import httpx


login_payload = {
    "email": "usermailv1@mail.ru",
    "password": "qwer123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response_data)
print(login_response.status_code)

headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_response_data = user_response.json()

print(user_response_data)
print(user_response.status_code)