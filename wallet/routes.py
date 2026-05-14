from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from db.database import get_db
from db.models import Wallet
from auth.dependencies import get_current_user

router = APIRouter()


@router.post("/deposit")
def deposit(data: dict, db: Session = Depends(get_db), current=Depends(get_current_user)):

    wallet = db.query(Wallet).filter(Wallet.user_id == current["user_id"]).first()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    amount = data["amount"]

    wallet.balance += amount
    db.commit()

    return {
        "message": "Deposit successful",
        "new_balance": wallet.balance
    }


def hold_funds(wallet, amount):
    if wallet.balance < amount:
        return False

    wallet.balance -= amount
    return True



@router.post("/release")
def release_funds(data: dict, db: Session = Depends(get_db)):

    wallet = db.query(Wallet).filter(Wallet.user_id == data["user_id"]).first()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    wallet.balance += data["amount"]

    db.commit()

    return {
        "message": "Funds released successfully"
    }


@router.post("/refund")
def refund(data: dict, db: Session = Depends(get_db)):

    wallet = db.query(Wallet).filter(Wallet.user_id == data["user_id"]).first()

    wallet.balance += data["amount"]

    db.commit()

    return {
        "message": "Refund processed",
        "amount_refunded": data["amount"]
    }



@router.get("/balance")
def get_balance(current=Depends(get_current_user), db: Session = Depends(get_db)):

    wallet = db.query(Wallet).filter(Wallet.user_id == current["user_id"]).first()

    return {
        "balance": wallet.balance
    }


class TransactionLog:
    logs = []

def log_transaction(user_id, type, amount):
    TransactionLog.logs.append({
        "user_id": user_id,
        "type": type,
        "amount": amount,
        "timestamp": datetime.utcnow()
    })


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    balance = Column(Float, default=0.0)