from db.models import User
from db.models import Wallet
from core.security import hash_password, verify_password, create_access_token

def create_user(db, user_data):
    user = User(
        full_name=user_data["full_name"],
        username=user_data["username"],
        phone=user_data["phone"],
        password=hash_password(user_data["password"]),
        state=user_data["state"],
        lga=user_data["lga"],
        role="buyer"
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db, username, password):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def login_token(user):
    return create_access_token({"sub": str(user.id), "role": user.role})


def create_user(db, user_data):
    user = User(
        full_name=user_data["full_name"],
        username=user_data["username"],
        phone=user_data["phone"],
        password=hash_password(user_data["password"]),
        state=user_data["state"],
        lga=user_data["lga"],
        role="buyer"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    # AUTO CREATE WALLET
    wallet = Wallet(user_id=user.id, balance=0.0)
    db.add(wallet)
    db.commit()

    return user