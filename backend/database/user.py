import random
import string


class User:
    def __init__(self):
        self.default = {"uid": None, "password": None, "name": None}

        self.results = []

    def random_characters(self, length):
        characters = string.ascii_lowercase + string.digits
        return "".join(random.choices(characters, k=length))

    def generate(self):
        # Generate 1 admin
        self.results.append(
            {**self.default, "uid": "admin", "password": "admin", "name": "admin"}
        )

        # Generate 9 users
        for _ in range(9):
            self.results.append(
                {
                    **self.default,
                    "uid": self.random_characters(8),
                    "password": self.random_characters(8),
                    "name": self.random_characters(8),
                }
            )

        return self.results
