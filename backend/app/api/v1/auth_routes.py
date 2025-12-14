# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.db.database import get_db
# from app.models.user import User
# from app.schemas.user_schema import UserCreate
# from app.core.security import hash_password, verify_password
# from app.core.auth import create_access_token

# router = APIRouter(prefix="/auth", tags=["Auth"])

# @router.post("/signup")
# def signup(user: UserCreate, db: Session = Depends(get_db)):
#     new_user = User(
#         username=user.username,
#         email=user.email,
#         password=hash_password(user.password)
#     )
#     db.add(new_user)
#     db.commit()
#     return {"message": "User created"}

# # @router.post("/login")
# # def login(email: str, password: str, db: Session = Depends(get_db)):
# #     user = db.query(User).filter(User.email == email).first()
# #     if not user or not verify_password(password, user.password):
# #         return {"error": "Invalid credentials"}

# #     token = create_access_token({"user_id": user.id})
# #     return {"access_token": token, "token_type": "bearer"}

# @router.post("/login")
# def login(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: Session = Depends(get_db)
# ):
#     user = db.query(User).filter(User.email == form_data.username).first()

#     if not user or not verify_password(form_data.password, user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     token = create_access_token({"user_id": user.id})
#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }


from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password, verify_password
from app.core.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})
    return {
        "access_token": token,
        "token_type": "bearer"
    }
