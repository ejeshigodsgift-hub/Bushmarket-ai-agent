from fastapi import FastAPI
from db.database import Base, engine

from auth.routes import router as auth_router
from users.routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bushmarket System")

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")

