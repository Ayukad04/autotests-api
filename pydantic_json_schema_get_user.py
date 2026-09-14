from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakes import get_random_email
from clients.users.private_users_client import get_private_users_client
from clients.private_http_builder import AuthenticationUserSchema

# Создаём публичный клиент
public_users_client = get_public_users_client()

# Формируем запрос на создание нового пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="123qwer",
    last_name="Федоров",
    first_name="Александр",
    middle_name="Владимирович"
)

# Отправляем запрос на создание пользователя и получаем ответ
create_user_response = public_users_client.create_user_api(create_user_request)

# Парсим ответ API в модель CreateUserResponseSchema
created_user = CreateUserResponseSchema.model_validate_json(create_user_response.text)

# Формируем данные для аутентификации созданного пользователя
auth_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Создаём приватный клиент с токеном созданного пользователя
private_users_client = get_private_users_client(auth_user)

# Извлекаем ID созданного пользователя
user_id = created_user.user.id

# Генерируем JSON-схему из модели GetUserResponseSchema
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Отправляем запрос на получение пользователя по ID
get_user_response = private_users_client.get_user_api(user_id)

# Парсим ответ API в модель GetUserResponseSchema
user = GetUserResponseSchema.model_validate_json(get_user_response.text)
print(user)

# Валидируем ответ API по JSON-схеме
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

# Удаляем email пользователя и проверяем работу функции validate_json_schema при отсутствии обязательного поля
# response_data = get_user_response.json()
# del response_data["user"]["email"]
# validate_json_schema(instance=response_data, schema=get_user_response_schema)
