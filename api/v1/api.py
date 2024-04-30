from fastapi import APIRouter

from api.v1.endpoints import moranguinho

api_router = APIRouter()
api_router.include_router(moranguinho.router, prefix="/moranguinho", tags=["moranguinhos"])

