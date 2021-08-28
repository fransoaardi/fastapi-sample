from fastapi import APIRouter

from fastapi_sample.src.router import predict

api_router = APIRouter()
api_router.include_router(predict.router, prefix="/predict")
