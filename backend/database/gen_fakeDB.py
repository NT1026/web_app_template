import json

from database.user import User

class GenFakeDB:
    def __init__(self):
        self.output = {
            "users": []
        }

    def generate_user(self):
        return User().generate()
    
    def generate(self):
        self.output["users"] = self.generate_user()
        with open("./database/fake_db.json", mode="w", encoding="utf-8") as file:
            json.dump(self.output, file, ensure_ascii=False, indent=4)
