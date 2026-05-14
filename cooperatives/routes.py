from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Cooperative, Wallet
from auth.dependencies import get_current_user

router = APIRouter()