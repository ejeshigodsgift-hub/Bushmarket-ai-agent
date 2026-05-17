from fastapi import APIRouter

router = APIRouter()

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


@router.get("/alerts")
def system_alerts():

    return {
        "alerts": [
            "Suspicious price detected",
            "Agent report mismatch",
            "Delayed cooperative funding"
        ]
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


@router.post("/update-gate-pass")
def update_gate_pass(data: dict, db):

    from db.models import ProductMarket

    market = db.query(ProductMarket).filter(
        ProductMarket.name == data["market_name"]
    ).first()

    if not market:
        return {"error": "Market not found"}

    market.gate_pass_fee = data["gate_pass_fee"]
    db.commit()

    return {
        "message": "Gate pass updated successfully",
        "market": market.name,
        "gate_pass_fee": market.gate_pass_fee
    }