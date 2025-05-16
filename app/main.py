from fastapi import FastAPI, HTTPException
from models import Task
from schemas import TaskCreate, TaskRead
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API TODO rodando!"}

@app.get("/tasks", response_model=list[TaskRead])
def list_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return tasks

@app.post("/tasks", response_model=TaskRead)
def create_task(task: TaskCreate):
    db = SessionLocal()
    db_task = Task(title=task.title, done=task.done)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task

@app.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task: TaskCreate):
    db = SessionLocal()
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db_task.title = task.title
    db_task.done = task.done
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(db_task)
    db.commit()
    db.close()
    return {"detail": "Tarefa removida com sucesso"}