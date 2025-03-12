from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.config import settings

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get("Authorization")
        if not api_key or api_key != f"Bearer {settings.MODELSLAB_API_KEY}":
            raise HTTPException(status_code=401, detail="Invalid or missing API key")
        return await call_next(request)
