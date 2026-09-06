import time
import random
import string


def get_random_email() -> str:
    return f"usermail.{time.time()}@mail.ru"


def generate_random_password() -> str:
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]

    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password.extend(random.choice(all_chars) for _ in range(7))

    random.shuffle(password)

    return "".join(password)
