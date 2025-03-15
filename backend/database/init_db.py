import json

from auth.passwd import get_password_hash
from models.user import User as UserModel

model = {
    "users": UserModel
}


class FakeDB:
    def __init__(self):
        with open("./database/fake_db.json", encoding="utf8") as file:
            self.data = json.load(file)

    async def create_entity_list(self, db_session):
        for table, entity_list in self.data.items():
            print(f"Creating {table}...")
            for entity in entity_list:
                if entity.get("password"):
                    entity["password"] = get_password_hash(entity["password"])
                
                row = model[table](**entity)
                db_session.add(row)
                