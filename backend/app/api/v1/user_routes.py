from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.follow import Follow
from app.core.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/{user_id}/follow")
def follow_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db.add(Follow(follower_id=current_user.id, following_id=user_id))
    db.commit()
    return {"message": "Followed"}

@router.post("/{user_id}/unfollow")
def unfollow_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db.query(Follow).filter(
        Follow.follower_id == current_user.id,
        Follow.following_id == user_id
    ).delete()
    db.commit()
    return {"message": "Unfollowed"}
