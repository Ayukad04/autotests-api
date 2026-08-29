from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient


class GetExercisesClient(TypedDict):
    """
    Описание структуры запроса на получение списка заданий определенного курса.
    """
    courseId: str


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int | None = 0
    minScore: int | None = 0
    orderIndex: int | None
    description: str
    estimatedTime: str | None = "PT0H0M"


class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesClient) -> Response:
        """
        Метод получения списка заданий для текущего курса.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)


    def get_exercise_api(self, exercise_id: str) -> Response :
        """
        Метод получения информации о задании по идентификатору.

        :params exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{exercise_id}")


    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод для создания задания.

        :param request: Словарь с id, title, courseId, maxScore, minScore, orderIndex,
                                  description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)


    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex,
                                  description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания по идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")