from fastapi import FastAPI
from app.middleware.auth_middleware import AuthMiddleware
from app.api.routes import router

app = FastAPI()
app.add_middleware(AuthMiddleware)
app.include_router(router)
