
from fastapi import APIRouter

from app.routes import customerRegistry, driverRegistry

api_router = APIRouter()
api_router.include_router(customerRegistry.router, tags=['customerRegistry'])
api_router.include_router(driverRegistry.router, tags=['driverRegistry'])

