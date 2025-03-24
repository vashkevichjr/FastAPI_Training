from sqlalchemy import select

from database import TaskOrm, new_session
from schemas import STaskAdd, STask


class TaskRepository:

    @classmethod
    async def add_task(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            new_task = TaskOrm(**task_dict)
            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.id

    @classmethod
    async def get_tasks(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas


