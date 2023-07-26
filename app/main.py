from fastapi import FastAPI
from typing import Union

from app.db import database, User

app = FastAPI(title="SAB Webservice")

@app.get("/")
async def read_root():
#     return {"test"}
    return await User.objects.all()

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# @app.on_event("shutdown")
# async def shutdown():
#     if database.is_connected:
#         await database.disconnect()