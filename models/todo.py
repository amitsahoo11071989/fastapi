from beanie import Document
from pydantic import BaseModel


class Todo(BaseModel):
    user: str
    title: str
    desc: str

    class Config:
        schema_extra= {
            "example":{
                "user": "Amit",
                "title": "1st todo item",
                "desc": "This is my first todo item in here"
            }
        }


class TodoUpdate(BaseModel):
    user: str
    title: str
    desc: str

    class Config:
        schema_extra = {
            "example": {
                "user": "",
                "title": "",
                "desc": ""
            }
        }
