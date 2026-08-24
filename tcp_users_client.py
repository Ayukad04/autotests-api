import socket

import random

users_messages = [
    "Привет, сервер!",
    "Как дела?",
    "Я хочу заказать пиццу.",
    "Пришлите мне список товаров.",
    "Спасибо за помощь!",
    "Мой заказ №12345 уже оплачен.",
    "Почему так долго?",
    "Можете повторить?",
    "До свидания!",
    "Сколько времени?"
]

# Создаем файл-счетчик, содержащий информацию о количестве отправленных сообщений
try:
    with open('counter.txt', 'r') as f:
        count = int(f.read().strip())
except FileNotFoundError:
    count = 1


random_message = random.choice(users_messages)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Сообщение от первого клиента всегда будет "Привет, сервер!", все последующие - рандомные
if count == 1:
    message = "Привет, сервер!"
else:
    message = random_message

client_socket.send(message.encode())
response = client_socket.recv(1024).decode()
print(response)

client_socket.close()

# Увеличиваем счетчик на 1
count += 1
with open('counter.txt', 'w') as f:
    f.write(str(count))
