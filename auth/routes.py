from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from auth.service import create_user, authenticate_user, login_token

router = APIRouter()

# SIGNUP
@router.post("/signup")
def signup(user: dict, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user["username"]).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = create_user(db, user)
    return {
        "message": "Account created successfully",
        "user_id": new_user.id
    }


# LOGIN
@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    user = authenticate_user(db, data["username"], data["password"])

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = login_token(user)

    return {
        "access_token": token,
        "token_type": "bearer"
    }