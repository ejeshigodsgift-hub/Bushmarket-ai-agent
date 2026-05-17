from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Cooperative

router = APIRouter()

@router.post("/approve-cooperative/{coop_id}")
def approve_cooperative(coop_id: int, db: Session = Depends(get_db)):

    coop = db.query(Cooperative).filter(Cooperative.id == coop_id).first()

    if not coop:
        raise HTTPException(status_code=404, detail="Not found")

    coop.status = "approved"
    db.commit()

    return {"message": "Cooperative approved"}


@router.post("/reject-cooperative/{coop_id}")
def reject_cooperative(coop_id: int, db: Session = Depends(get_db)):

    coop = db.query(Cooperative).filter(Cooperative.id == coop_id).first()

    if not coop:
        raise HTTPException(status_code=404, detail="Not found")

    coop.status = "rejected"
    db.commit()

    return {"message": "Cooperative rejected"}