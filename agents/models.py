from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from db.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    region = Column(String, nullable=False)
    status = Column(String, default="pending")  # pending / active / rejected

    created_at = Column(DateTime, default=datetime.utcnow)