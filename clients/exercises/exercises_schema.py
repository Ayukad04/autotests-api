from pydantic import BaseModel, Field, ConfigDict


# Описание структуры задания
class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


# Добавили описание структуры ответа списка заданий конкретного курса
class GetExercisesResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий определенного курса.
    """
    course_id: str = Field(alias="courseId")


class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")



class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание задания.
    """
    exercise: ExerciseSchema


class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление задания.
    """
    exercise: ExerciseSchema