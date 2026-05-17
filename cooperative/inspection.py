from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/inspection-report")
def inspection_report(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):

    required = ["quality_status", "quantity_verified", "price_confirmed", "recommendation"]

    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} is required")

    return {
        "message": "Inspection report submitted",
        "data": data,
        "status": "awaiting_admin_decision"
    }


@router.post("/verify-report")
def verify_report(data: dict, user=Depends(get_current_user)):

    if "status" not in data:
        raise HTTPException(status_code=400, detail="status is required")

    if data["status"] == "approved":
        return {
            "message": "Report approved",
            "action": "proceed to procurement"
        }

    return {
        "message": "Report rejected",
        "action": "request new sourcing"
    }