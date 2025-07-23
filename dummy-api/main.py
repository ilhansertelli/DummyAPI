

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

print(Path(__file__).resolve().parent)
print(sys.path)
from fastapi import FastAPI, Header
from appAPI.models import UserRegister, UserLogin
from appAPI.auth import register_user, login_user, get_current_user

app = FastAPI()

@app.post("/register")
def register(user: UserRegister):
    return register_user(user)

@app.post("/login")
def login(user: UserLogin):
    return login_user(user)

@app.get("/me")
def read_current_user(Authorization: str = Header(...)):
    return get_current_user(Authorization)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=88, reload=True)