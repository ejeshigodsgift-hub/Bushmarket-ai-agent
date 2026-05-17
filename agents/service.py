def assign_task(agent_id: int, task: dict):

    return {
        "agent_id": agent_id,
        "task": task,
        "status": "assigned"
    }


def complete_task(agent_id: int, task_id: int):

    return {
        "agent_id": agent_id,
        "task_id": task_id,
        "status": "completed"
    }