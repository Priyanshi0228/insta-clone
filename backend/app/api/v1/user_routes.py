# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.db.database import get_db
# from app.models.follow import Follow
# from app.core.auth import get_current_user

# router = APIRouter(prefix="/users", tags=["Users"])

# @router.post("/{user_id}/follow")
# def follow_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
#     db.add(Follow(follower_id=current_user.id, following_id=user_id))
#     db.commit()
#     return {"message": "Followed"}

# @router.post("/{user_id}/unfollow")
# def unfollow_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
#     db.query(Follow).filter(
#         Follow.follower_id == current_user.id,
#         Follow.following_id == user_id
#     ).delete()
#     db.commit()
#     return {"message": "Unfollowed"}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.follow import Follow
from app.models.user import User
from app.models.post import Post
from app.core.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

# Follow a user
@router.post("/{user_id}/follow")
def follow_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db.add(Follow(follower_id=current_user.id, following_id=user_id))
    db.commit()
    return {"message": "Followed"}

# Unfollow a user
@router.post("/{user_id}/unfollow")
def unfollow_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db.query(Follow).filter(
        Follow.follower_id == current_user.id,
        Follow.following_id == user_id
    ).delete()
    db.commit()
    return {"message": "Unfollowed"}

# Get current logged-in user info
@router.get("/me")
def get_me(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user = db.query(User).filter(User.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get user posts
    posts = db.query(Post).filter(Post.user_id == user.id).all()
    
    # Count followers and following
    followers_count = db.query(Follow).filter(Follow.following_id == user.id).count()
    following_count = db.query(Follow).filter(Follow.follower_id == user.id).count()

    return {
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "followers_count": followers_count,
            "following_count": following_count,
        },
        "posts": [
            {
                "id": post.id,
                "image_url": post.image_url,
                "caption": post.caption,
                "likes_count": post.likes_count
            } for post in posts
        ]
    }
