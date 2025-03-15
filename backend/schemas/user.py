from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    uid: str = Field(min_length=1, max_length=10)
    password: str = Field(min_length=6, max_length=20)
    name: str = Field(min_length=1, max_length=50)

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "uid": "user",
                    "password": "password",
                    "name": "user"
                }
            ]
        }
    }


class UserRead(BaseModel):
    uid: str
    name: str


class UserUpdate(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=50)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "user1"
                }
            ]
        }
    }


class UserUpdatePassword(BaseModel):
    password: str = Field(min_length=6, max_length=20)
