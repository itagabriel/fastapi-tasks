from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    done: bool = False

class TaskRead(TaskCreate):
    id: int

    class Config:
        orm_mode = True