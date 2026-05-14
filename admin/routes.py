from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models import Cooperative
from db.database import get_db
from db.models import Product
from db.models import Wallet
from auth.dependencies import get_current_user

router = APIRouter()




@router.post("/add-product")
def add_product(data: dict, db: Session = Depends(get_db)):

    product = Product(
        name=data["name"],
        category=data["category"],
        price=data["price"],
        unit=data["unit"],
        image_url=data["image_url"],
        location=data["location"],
        available_qty=data["available_qty"]
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return {
        "message": "Product published successfully",
        "product_id": product.id
    }




@router.post("/approve-cooperative/{coop_id}")
def approve_cooperative(coop_id: int, db: Session = Depends(get_db)):

    coop = db.query(Cooperative).filter(Cooperative.id == coop_id).first()

    if not coop:
        raise HTTPException(status_code=404, detail="Not found")

    coop.status = "approved"

    db.commit()

    return {
        "message": "Cooperative approved"
    }


@router.post("/reject-cooperative/{coop_id}")
def reject_cooperative(coop_id: int, db: Session = Depends(get_db)):

    coop = db.query(Cooperative).filter(Cooperative.id == coop_id).first()

    coop.status = "rejected"

    db.commit()

    return {
        "message": "Cooperative rejected"
    }


@router.post("/release-funds")
def release_funds(data: dict, db: Session = Depends(get_db)):

    wallet = db.query(Wallet).filter(Wallet.user_id == data["user_id"]).first()

    wallet.balance += data["amount"]

    db.commit()

    return {
        "message": "Funds released from escrow"
    }


@router.post("/approve-procurement")
def approve_procurement(data: dict):

    return {
        "message": "Procurement approved",
        "status": "agents proceed to purchase"
    }


@router.post("/assign-agent")
def assign_agent(data: dict):

    return {
        "message": "Agent assigned",
        "agent_id": data["agent_id"],
        "task": data["task"]
    }


@router.get("/alerts")
def system_alerts():

    return {
        "alerts": [
            "Suspicious price detected",
            "Agent report mismatch",
            "Delayed cooperative funding"
        ]
    }


@router.get("/dashboard")
def admin_dashboard():

    return {
        "system_status": "operational",
        "pending_cooperatives": [],
        "active_agents": [],
        "pending_products": [],
        "wallet_activity": [],
        "alerts": []
    }





