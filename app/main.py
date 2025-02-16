from fastapi import FastAPI
from .routers import task
from shared.store import store

store.load()

app = FastAPI()
app.include_router(task.router)


@app.get("/health")
async def home():
    return "ok"
