from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Cooperative, Wallet
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/create")
def create_cooperative(data: dict, db: Session = Depends(get_db), current=Depends(get_current_user)):

    coop = Cooperative(
        name=data["name"],
        product_category=data["product_category"],
        target_qty=data["target_qty"],
        max_members=data["max_members"],
        contribution_per_member=data["contribution_per_member"],
        status="funding"
    )

    db.add(coop)
    db.commit()
    db.refresh(coop)

    return {
        "message": "Cooperative created",
        "cooperative_id": coop.id
    }


@router.post("/join/{coop_id}")
def join_cooperative(coop_id: int, db: Session = Depends(get_db), current=Depends(get_current_user)):

    coop = db.query(Cooperative).filter(Cooperative.id == coop_id).first()
    wallet = db.query(Wallet).filter(Wallet.user_id == current["user_id"]).first()

    if not coop:
        raise HTTPException(status_code=404, detail="Cooperative not found")

    if wallet.balance < coop.contribution_per_member:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # ESCROW DEDUCTION
    wallet.balance -= coop.contribution_per_member

    db.commit()

    return {
        "message": "Joined cooperative successfully",
        "status": "funds locked in escrow",
        "coop_id": coop.id
    }


@router.get("/{coop_id}")
def get_cooperative(coop_id: int, db: Session = Depends(get_db)):

    coop = db.query(Cooperative).filter(Cooperative.id == coop_id).first()

    if not coop:
        raise HTTPException(status_code=404, detail="Not found")

    return {
        "id": coop.id,
        "name": coop.name,
        "product_category": coop.product_category,
        "target_qty": coop.target_qty,
        "max_members": coop.max_members,
        "contribution_per_member": coop.contribution_per_member,
        "status": coop.status
    }



def calculate_allocation(total_qty, member_contribution, total_contributions):

    share = (member_contribution / total_contributions) * total_qty

    return round(share, 2)


@router.get("/summary/{coop_id}")
def coop_summary(coop_id: int, db: Session = Depends(get_db)):

    coop = db.query(Cooperative).filter(Cooperative.id == coop_id).first()

    if not coop:
        raise HTTPException(status_code=404, detail="Not found")

    estimated_total = coop.max_members * coop.contribution_per_member

    return {
        "name": coop.name,
        "product_category": coop.product_category,
        "estimated_total_fund": estimated_total,
        "contribution_per_member": coop.contribution_per_member,
        "max_members": coop.max_members
    }


@router.post("/expire/{coop_id}")
def expire_cooperative(coop_id: int, db: Session = Depends(get_db)):

    coop = db.query(Cooperative).filter(Cooperative.id == coop_id).first()

    if not coop:
        raise HTTPException(status_code=404, detail="Not found")

    coop.status = "failed_refunded"

    db.commit()

    return {
        "message": "Cooperative expired and marked for refund"
    }


@router.post("/ai-create")
def ai_create(data: dict):

    return {
        "message": "AI cooperative draft created",
        "draft": data,
        "next_step": "user confirmation required"
    }