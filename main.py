from traceback import print_tb
from typing import Annotated

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel, ConfigDict
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from schemas import STaskAdd


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("База выключена")


app = FastAPI(lifespan=lifespan)

tasks = []

@app.post("/tasks")
async def add_tasks(
        task: Annotated[STaskAdd, Depends()]
):
    tasks.append(task)
    return {"ok":True}


