from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse, Response
from shared.store import Store
from shared.models import Task
from ..dependencies import get_store
from shared.exceptions import TaskNotFoundException
from ..requests import AddTaskRequest

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Task,
)
async def add_task(
    req: AddTaskRequest,
    store: Store = Depends(get_store),
):
    task = Task(
        id=4,
        title=req.title,
        done=False,
    )
    task = store.add_task(task)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=task.model_dump())


@router.get(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    response_model=Task,
)
async def get_task(
    task_id: int,
    store: Store = Depends(get_store),
):
    try:
        task = store.get_task(task_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=task.model_dump())
    except TaskNotFoundException as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[Task],
)
async def list_tasks(
    store: Store = Depends(get_store),
):
    tasks = store.list_tasks()
    tasks = [task.model_dump() for task in tasks]
    return JSONResponse(status_code=status.HTTP_200_OK, content=tasks)


@router.post(
    "/{task_id}/complete",
    status_code=status.HTTP_200_OK,
    response_model=Task,
)
async def complete_task(
    task_id: int,
    store: Store = Depends(get_store),
):
    try:
        task = store.complete_task(task_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=task.model_dump())
    except TaskNotFoundException as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.post(
    "/{task_id}/incomplete",
    status_code=status.HTTP_200_OK,
    response_model=Task,
)
async def incomplete_task(
    task_id: int,
    store: Store = Depends(get_store),
):
    try:
        task = store.incomplete_task(task_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=task.model_dump())
    except TaskNotFoundException as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def remove_task(
    task_id: int,
    store: Store = Depends(get_store),
):
    try:
        store.remove_task(task_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except TaskNotFoundException as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
