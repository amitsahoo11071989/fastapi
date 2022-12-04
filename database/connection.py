from typing import  Any, List, Optional
from beanie import init_beanie,PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings, BaseModel
from models.todo import Todo


class Settings(BaseModel):
    DATABASE_URL = Optional[str]= None

    async def initialize_database(self):
        client= AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database = client.get_default_database(),
                          document_models=[Todo])

    class Config:
        env_file = ".env"


class Database:
    def __int__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id:PydanticObjectId)-> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self)-> List[Any]:
        docs= await self.model.find_all().to_list()
        if docs:
            return docs
        return False


    async def update(self, id: PydanticObjectId, body: BaseModel)-> Any:
        doc_id = id
        des_body = body.dict()

        des_body = {k:v for k,v in des_body.items() if v is not None}
        
