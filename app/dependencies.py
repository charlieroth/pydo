from typing import Annotated
from fastapi import Depends
from shared.store import store, Store


def get_store() -> Store:
    return store


StoreDep = Annotated[Store, Depends(get_store)]
