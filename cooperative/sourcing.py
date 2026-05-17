from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/submit-sourcing")
def submit_sourcing(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):

    required = ["supplier_name", "product", "location", "price", "available_qty"]

    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} is required")

    return {
        "message": "Sourcing report submitted",
        "data": data,
        "status": "pending_admin_review"
    }