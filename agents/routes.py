from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import User
from agents.models import Agent
from auth.dependencies import get_current_user
from agents.service import format_agent_response

router = APIRouter(prefix="/agents", tags=["Agents"])


# =========================
# 1. AGENT SIGN-UP (APPLICATION)
# =========================
@router.post("/apply")
def apply_agent(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):

    # REQUIREMENTS CHECK
    if not data.get("region"):
        raise HTTPException(status_code=400, detail="region is required")

    # CHECK IF ALREADY APPLIED
    existing = db.query(Agent).filter(Agent.user_id == user.id).first()

    if existing:
        raise HTTPException(status_code=400, detail="Agent application already exists")

    agent = Agent(
        user_id=user.id,
        region=data["region"],
        status="pending"
    )

    db.add(agent)
    db.commit()
    db.refresh(agent)

    return {
        "message": "Agent application submitted",
        "agent": format_agent_response(agent)
    }


# =========================
# 2. ADMIN APPROVE AGENT
# =========================
@router.patch("/approve/{agent_id}")
def approve_agent(agent_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):

    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent.status = "active"

    # upgrade user role
    user_obj = db.query(User).filter(User.id == agent.user_id).first()
    user_obj.role = "agent"

    db.commit()

    return {
        "message": "Agent approved successfully",
        "agent": format_agent_response(agent)
    }


# =========================
# 3. REJECT AGENT
# =========================
@router.patch("/reject/{agent_id}")
def reject_agent(agent_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):

    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent.status = "rejected"
    db.commit()

    return {
        "message": "Agent rejected",
        "agent": format_agent_response(agent)
    }


# =========================
# 4. GET AGENT PROFILE
# =========================
@router.get("/{agent_id}")
def get_agent(agent_id: int, db: Session = Depends(get_db)):

    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    return format_agent_response(agent)


# =========================
# 5. AGENT DASHBOARD
# =========================
@router.get("/dashboard/{agent_id}")
def agent_dashboard(agent_id: int, db: Session = Depends(get_db)):

    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    return {
        "agent": format_agent_response(agent),
        "active_tasks": [],
        "completed_tasks": [],
        "notifications": []
    }