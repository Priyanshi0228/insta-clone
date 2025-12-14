from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.auth import get_current_user
from app.models.post import Post
from app.models.follow import Follow

router = APIRouter(prefix="/feed", tags=["Feed"])

@router.get("/")
def get_feed(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Post).join(
        Follow, Post.user_id == Follow.following_id
    ).filter(
        Follow.follower_id == user.id
    ).order_by(Post.created_at.desc()).all()
