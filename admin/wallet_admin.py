from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Wallet

router = APIRouter()

@router.post("/release-funds")
def release_funds(data: dict, db: Session = Depends(get_db)):

    wallet = db.query(Wallet).filter(
        Wallet.user_id == data["user_id"]
    ).first()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    wallet.balance += data["amount"]
    db.commit()

    return {"message": "Funds released from escrow"}