from models import users
from db import database
from schemas import UserCreate, UserUpdate

async def create_user(user: UserCreate):
    query = users.insert().values(name=user.name, email=user.email)
    user_id = await database.execute(query)
    return {**user.model_dump(), "id": user_id}


async def list_users():
    query = users.select()
    return await database.fetch_all(query)


async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


async def update_user(user_id: int, user: UserUpdate):
    query = users.update().where(users.c.id == user_id).values(name=user.name, email=user.email)
    await database.execute(query)
    return {**user.model_dump(), "id": user_id}


async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    return await database.execute(query)
