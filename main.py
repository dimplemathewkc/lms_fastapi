from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="My API",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="2.5.0",
    contact={
        "name": "Dimple Mathew",
    }

)

users = [

]


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@app.get("/", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    # validate if the user has these fields
    users.append(user)
    return user


# url path params
@app.get("/users/{id}")
async def get_user(id: int):
    return users[id]
