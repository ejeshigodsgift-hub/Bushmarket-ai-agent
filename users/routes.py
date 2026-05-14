from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import User, Wallet
from auth.dependencies import get_current_user

router = APIRouter()


# GET USER PROFILE
@router.get("/me")
def get_profile(current=Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == current["user_id"]).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "full_name": user.full_name,
        "username": user.username,
        "phone": user.phone,
        "state": user.state,
        "lga": user.lga,
        "role": user.role
    }


# UPDATE PROFILE
@router.put("/update")
def update_profile(data: dict, current=Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == current["user_id"]).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.full_name = data.get("full_name", user.full_name)
    user.state = data.get("state", user.state)
    user.lga = data.get("lga", user.lga)

    db.commit()

    return {"message": "Profile updated successfully"}


# USER DASHBOARD SUMMARY
@router.get("/dashboard")
def dashboard(current=Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == current["user_id"]).first()
    wallet = db.query(Wallet).filter(Wallet.user_id == user.id).first()

    if not wallet:
        wallet = Wallet(user_id=user.id, balance=0)
        db.add(wallet)
        db.commit()

    return {
        "user": {
            "full_name": user.full_name,
            "state": user.state,
            "lga": user.lga
        },
        "wallet_balance": wallet.balance
    }