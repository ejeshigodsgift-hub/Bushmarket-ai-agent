from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Product
from auth.dependencies import get_current_user

router = APIRouter()