from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.auth import get_current_user
from app.models.post import Post
from app.models.like import Like
from app.models.comment import Comment
from app.schemas.post_schema import PostCreate
from app.schemas.comment_schema import CommentCreate

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/")
def create_post(post: PostCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_post = Post(user_id=user.id, **post.dict())
    db.add(new_post)
    db.commit()
    return {"message": "Post created"}

@router.post("/{post_id}/like")
def like_post(post_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db.add(Like(user_id=user.id, post_id=post_id))
    db.commit()
    return {"message": "Liked"}

@router.post("/{post_id}/unlike")
def unlike_post(post_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db.query(Like).filter(
        Like.user_id == user.id,
        Like.post_id == post_id
    ).delete()
    db.commit()
    return {"message": "Unliked"}

@router.post("/{post_id}/comment")
def comment_post(post_id: int, comment: CommentCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db.add(Comment(user_id=user.id, post_id=post_id, text=comment.text))
    db.commit()
    return {"message": "Comment added"}
