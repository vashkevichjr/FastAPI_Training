from traceback import print_tb
from typing import Annotated

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel, ConfigDict
from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")

app = FastAPI(lifespan=lifespan)

class STaskAdd(BaseModel):
    name: str
    description: str | None = None

class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

tasks = []

@app.post("/tasks")
async def add_tasks(
        task: Annotated[STaskAdd, Depends()]
):
    tasks.append(task)
    return {"ok":True}


