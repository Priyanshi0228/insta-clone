from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.api.v1 import auth_routes, user_routes, post_routes, feed_routes
from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(bind=engine)

app = FastAPI(title="Instagram Mini Clone")

# Add CORS middleware
origins = [
    "http://localhost:5173",  # Vite frontend
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow your frontend
    allow_credentials=True,
    allow_methods=["*"],          # Allow all methods (GET, POST, OPTIONS)
    allow_headers=["*"],          # Allow all headers
)

app.include_router(auth_routes.router, prefix="/api/v1")
app.include_router(user_routes.router, prefix="/api/v1")
app.include_router(post_routes.router, prefix="/api/v1")
app.include_router(feed_routes.router, prefix="/api/v1")
