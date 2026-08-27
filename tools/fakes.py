import time


def get_random_email() -> str:
    return f"usermail.{time.time()}@mail.ru"