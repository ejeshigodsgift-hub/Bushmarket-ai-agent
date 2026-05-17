def format_agent_response(agent):
    return {
        "agent_id": agent.id,
        "user_id": agent.user_id,
        "region": agent.region,
        "status": agent.status
    }