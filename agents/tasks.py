from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from auth.dependencies import get_current_user

router = APIRouter(prefix="/agents/tasks", tags=["Agent Tasks"])


# =========================
# 1. ASSIGN TASK (ADMIN ONLY)
# =========================
@router.post("/assign")
def assign_task(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):

    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    return {
        "message": "Task assigned",
        "task": {
            "agent_id": data["agent_id"],
            "product": data["product"],
            "location": data["location"],
            "quantity": data["quantity"],
            "deadline": data["deadline"],
            "status": "assigned"
        }
    }


# =========================
# 2. VIEW MY TASKS (AGENT)
# =========================
@router.get("/my-tasks")
def my_tasks(user=Depends(get_current_user)):

    if user.role != "agent":
        raise HTTPException(status_code=403, detail="Agents only")

    return {
        "agent_id": user.id,
        "tasks": []
    }


# =========================
# 3. UPDATE TASK STATUS
# =========================
@router.patch("/update-status/{task_id}")
def update_task_status(task_id: int, data: dict, user=Depends(get_current_user)):

    if user.role != "agent":
        raise HTTPException(status_code=403, detail="Agents only")

    if "status" not in data:
        raise HTTPException(status_code=400, detail="status required")

    return {
        "message": "Task updated",
        "task_id": task_id,
        "new_status": data["status"]
    }


# =========================
# 4. SUBMIT TASK REPORT
# =========================
@router.post("/submit-report/{task_id}")
def submit_report(task_id: int, data: dict, user=Depends(get_current_user)):

    if user.role != "agent":
        raise HTTPException(status_code=403, detail="Agents only")

    required = ["report", "price_found", "availability"]

    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} required")

    return {
        "message": "Report submitted",
        "task_id": task_id,
        "report": data,
        "status": "pending_verification"
    }