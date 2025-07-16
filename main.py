from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Query, HTTPException
from db import database, engine, metadata
from schemas import UserCreate, User, UserUpdate
import crud


metadata.create_all(engine)

# Lifespan context
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    print("✅ Database connected.")
    yield
    await database.disconnect()
    print("🛑 Database disconnected.")

# Create a FastAPI application
app = FastAPI(lifespan=lifespan)


@app.post("/users", response_model=User)
async def create(user: UserCreate):
    return await crud.create_user(user)


@app.get("/users", response_model=list[User])
async def read_users():
    return await crud.list_users()


@app.get("/users/{user_id}", response_model=User)
async def read(user_id: int):
    user = await crud.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
# @app.patch("/users/{user_id}", response_model=User)
async def update(user_id: int, user: UserUpdate):
    exist_user = await crud.get_user(user_id)
    if not exist_user:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.update_user(user_id, user)


@app.delete("/users/{user_id}")
async def delete(user_id: int):
    exist_user = await crud.delete_user(user_id)
    if not exist_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

#-------------------
# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/a/")
def read_root(request: Request):
    return {"method": request.method, "url": request.url}


@app.get("/items/")
def read_items(q: str = Query(..., min_length = 3, max_length = 50)):
    print(q, "q")
    results = []
    return results