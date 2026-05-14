from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models import ProductMarket
from db.database import get_db
from db.models import Product
from auth.dependencies import get_current_user

router = APIRouter()


@router.get("/gallery")
def commodity_gallery():
    return {
        "markets": [
            "Rice Market",
            "Palm Oil Market",
            "Beans Market",
            "Fish Market",
            "Yam and Potatoes Market",
            "Cocoa Market",
            "Ogbono & Egusi Market",
            "Groundnut Market",
            "Honey Market",
            "Natural Spices Market",
            "Garri Market",
            "Maize Market",
            "Ginger Market"
        ]
    }


@router.get("/nearest/{category}")
def nearest_market(category: str, current=Depends(get_current_user)):
    return {
        "category": category,
        "location": "auto-detected LGA market",
        "message": "Showing nearest market based on user LGA",
        "products": []
    }


@router.get("/market/{category}")
def market_view(category: str, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.category == category).all()

    return {
        "category": category,
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "unit": p.unit,
                "image": p.image_url,
                "location": p.location,
                "available_qty": p.available_qty
            }
            for p in products
        ]
    }


@router.get("/search")
def search_products(query: str, db: Session = Depends(get_db)):
    results = db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()

    return {
        "query": query,
        "results": [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "unit": p.unit,
                "image": p.image_url,
                "category": p.category
            }
            for p in results
        ]
    }


@router.get("/filter")
def filter_products(
    category: str = None,
    min_price: float = None,
    max_price: float = None,
    db: Session = Depends(get_db)
):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if min_price:
        query = query.filter(Product.price >= min_price)

    if max_price:
        query = query.filter(Product.price <= max_price)

    products = query.all()

    return {
        "filters": {
            "category": category,
            "min_price": min_price,
            "max_price": max_price
        },
        "results": [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "unit": p.unit,
                "image": p.image_url
            }
            for p in products
        ]
    }

@router.get("/ai-suggest")
def ai_suggest(lga: str, interest: str):
    return {
        "lga": lga,
        "suggestions": [
            f"Best {interest} market near {lga}",
            f"Cheapest {interest} deals available",
            f"Active cooperatives buying {interest}"
        ]
    }

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    unit = Column(String)
    image_url = Column(String)
    location = Column(String)  # LGA or market zone
    available_qty = Column(Float)


@router.post("/checkout")
def checkout(data: dict, db: Session = Depends(get_db)):

    market = db.query(ProductMarket).filter(
        ProductMarket.name == data["market_name"]
    ).first()

    if not market:
        raise HTTPException(status_code=404, detail="Market not found")

    product_total = data["product_total"]
    delivery_fee = data["delivery_fee"]

    gate_pass_fee = market.gate_pass_fee

    final_total = (
        product_total
        + delivery_fee
        + gate_pass_fee
    )

    return {
        "market": market.name,
        "product_total": product_total,
        "delivery_fee": delivery_fee,
        "gate_pass_fee": gate_pass_fee,
        "final_total": final_total,
        "message": "Gate pass automatically added to checkout"
    }
