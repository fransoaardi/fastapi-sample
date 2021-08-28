from fastapi import FastAPI
from fastapi_sample.src.router.router import api_router

app = FastAPI()
app.include_router(api_router)
