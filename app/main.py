from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routes.api import router as api_router

app = FastAPI(title="SAB Webservice")

origins = ["https://app.fastapi.test"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

#
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# @app.post("/entity/{type}", response_model=EntityModel)
# def create_entity(entity: EntityCreate, db: Session = Depends(get_db)):
#    return {"test"} #Repository.create_entity(db, email=entity.type)
#
# # @app.on_event("startup")
# # async def startup():
# #     if not database.is_connected:
# #         await database.connect()
# #     # create a dummy entry
# #     await User.objects.get_or_create(email="test@test.com")
# #
# @app.get("/")
# def read_root():
#     return {"test"}
# #
# # # @app.on_event("shutdown")
# # # async def shutdown():
# # #     if database.is_connected:
# # #         await database.disconnect()