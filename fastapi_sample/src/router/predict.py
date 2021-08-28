from fastapi import APIRouter

router = APIRouter()


@router.get("")
def predict():
    return {"Hello": "World"}
