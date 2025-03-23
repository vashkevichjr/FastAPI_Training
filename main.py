from typing import Optional, Annotated

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel
app = FastAPI()

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks")
async def add_tasks(
        task: Annotated[STaskAdd, Depends()]
):
    tasks.append(task)
    return {"ok":True}


