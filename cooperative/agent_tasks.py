from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/assign-task")
def assign_task(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):

    required = ["agent_id", "product", "location", "quantity", "deadline"]

    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} is required")

    return {
        "message": "Task assigned to agent",
        "task": {
            "agent_id": data["agent_id"],
            "product": data["product"],
            "location": data["location"],
            "quantity": data["quantity"],
            "deadline": data["deadline"]
        }
    }