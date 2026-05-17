from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from agents.models import Agent
from auth.dependencies import get_current_user

router = APIRouter(prefix="/agents", tags=["Agents"])


# CREATE AGENT
@router.post("/create")
def create_agent(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):

    agent = Agent(
        user_id=data["user_id"],
        region=data["region"],
        status="active"
    )

    db.add(agent)
    db.commit()
    db.refresh(agent)

    return {
        "message": "Agent created successfully",
        "agent_id": agent.id
    }


# GET AGENT PROFILE
@router.get("/{agent_id}")
def get_agent(agent_id: int, db: Session = Depends(get_db)):

    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    return agent


# UPDATE AGENT STATUS
@router.patch("/status/{agent_id}")
def update_status(agent_id: int, data: dict, db: Session = Depends(get_db)):

    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent.status = data["status"]
    db.commit()

    return {"message": "Status updated", "status": agent.status}