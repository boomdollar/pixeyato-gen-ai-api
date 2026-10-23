import secrets
from fastapi import Header, HTTPException
from app.config import API_KEY
async def verify_api_key(x_api_key: str = Header(default="")):
    if API_KEY and not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(status_code=401, detail="API key tidak valid.")
