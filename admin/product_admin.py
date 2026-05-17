from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Product

router = APIRouter()

@router.post("/add-product")
def add_product(data: dict, db: Session = Depends(get_db)):

    product = Product(
        name=data["name"],
        category=data["category"],
        price=data["price"],
        unit=data["unit"],
        image_url=data["image_url"],
        location=data["location"],
        available_qty=data["available_qty"]
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return {
        "message": "Product published successfully",
        "product_id": product.id
    }