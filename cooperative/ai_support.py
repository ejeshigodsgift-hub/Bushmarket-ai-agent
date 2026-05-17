from fastapi import APIRouter

router = APIRouter()

@router.get("/ai-support")
def ai_support(region: str, product: str):

    return {
        "region": region,
        "product": product,
        "suggestions": [
            "Nearby suppliers detected",
            "Cheapest market options available",
            "High supply zone identified"
        ]
    }