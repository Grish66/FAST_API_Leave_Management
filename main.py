from fastapi import FastAPI
from database import Base,engine
from routers.leave import router as leave_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(leave_router, prefix = "/api/v1", tags=['Leave Requests'])