import uuid
from pydantic import BaseModel, Field, EmailStr, SecretStr, field_serializer

from tools.fakes import fake, generate_random_password


# Базовый класс с общими полями
class UserBaseSchema(BaseModel):
    email: EmailStr = Field(default_factory=get_random_email)
    last_name: str = Field(alias="lastName", min_length=3, max_length=20)
    first_name: str = Field(alias="firstName", min_length=2, max_length=20)
    """
    Поле middle_name имеет значение по умолчанию "", т.к. у человека может не быть отчества, но согласно
    Swagger поле является обязательным
    """
    middle_name: str = Field(alias="middleName", default="", min_length=0, max_length=25)


# Создаем модель пользователя
class UserSchema(UserBaseSchema):
    id: str


# Создаем модель запроса на создание пользователя
class CreateUserRequestSchema(UserBaseSchema):
    password: SecretStr = Field(default_factory=generate_random_password, min_length=8)

    """
    Создадим сериализатор, что бы при преобразовании модели в словарь или JSON, 
    пароль отображался как маска **********
    """

    @field_serializer("password")
    def serialize_password(self, value: SecretStr) -> str:
        return "**********"


# Создаем модель ответа на создание пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema


# Инициализируем модель CreateUserRequestSchema через распаковку словаря

create_user_dict = {
    "lastName": "Петров",
    "firstName": "Андрей",
    "middleName": "Викторович"
}

user = CreateUserRequestSchema(**create_user_dict)

print(user.model_dump())
print(user.model_dump_json())
