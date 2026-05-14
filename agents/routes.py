from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from auth.dependencies import get_current_user

router = APIRouter()


class Agent:
    def __init__(self, user_id, region, status="active"):
        self.user_id = user_id
        self.region = region
        self.status = status


@router.post("/assign-task")
def assign_task(data: dict):

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


@router.post("/submit-sourcing")
def submit_sourcing(data: dict):

    return {
        "message": "Sourcing report submitted",
        "supplier_name": data["supplier_name"],
        "product": data["product"],
        "location": data["location"],
        "price": data["price"],
        "available_qty": data["available_qty"],
        "status": "pending_admin_review"
    }


@router.post("/inspection-report")
def inspection_report(data: dict):

    return {
        "message": "Inspection report submitted",
        "quality_status": data["quality_status"],
        "quantity_verified": data["quantity_verified"],
        "price_confirmed": data["price_confirmed"],
        "recommendation": data["recommendation"],  # approved / reject / revise
        "status": "awaiting_admin_decision"
    }


@router.get("/dashboard/{agent_id}")
def agent_dashboard(agent_id: int):

    return {
        "agent_id": agent_id,
        "active_tasks": [],
        "completed_tasks": [],
        "pending_reports": [],
        "status": "active"
    }


@router.get("/ai-support")
def ai_support(region: str, product: str):

    return {
        "region": region,
        "product": product,
        "suggestions": [
            "Nearby suppliers detected",
            "Cheapest market options available",
            "High supply zone identified"
        ]
    }


@router.post("/verify-report")
def verify_report(data: dict):

    if data["status"] == "approved":
        return {
            "message": "Report approved",
            "action": "proceed to procurement"
        }

    return {
        "message": "Report rejected",
        "action": "request new sourcing"
    }


