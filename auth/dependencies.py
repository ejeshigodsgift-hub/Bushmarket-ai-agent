from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from core.config import settings

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        payload = jwt.decode(
            token.credentials,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {"user_id": user_id}

    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid")