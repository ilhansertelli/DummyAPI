from fastapi import HTTPException
from appAPI.models import UserRegister, UserLogin, UserOut

# Dummy user storage
users = {}

def register_user(user: UserRegister):
    if user.email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.email] = {"username": user.username, "password": user.password}
    return {"message": "User registered successfully"}

def login_user(user: UserLogin):
    db_user = users.get(user.email)
    if not db_user or db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": f"dummy-token-for-{user.email}"}

def get_current_user(token: str):
    for email, data in users.items():
        if f"dummy-token-for-{email}" == token:
            return UserOut(username=data["username"], email=email)
    raise HTTPException(status_code=401, detail="Invalid token")
