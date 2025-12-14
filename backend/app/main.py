from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.api.v1 import auth_routes, user_routes, post_routes, feed_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Instagram Mini Clone")

app.include_router(auth_routes.router, prefix="/api/v1")
app.include_router(user_routes.router, prefix="/api/v1")
app.include_router(post_routes.router, prefix="/api/v1")
app.include_router(feed_routes.router, prefix="/api/v1")
