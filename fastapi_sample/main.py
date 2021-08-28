import uvicorn
from fastapi_sample.src.app.app import app


def run():
    uvicorn.run("fastapi_sample.main:app", host="0.0.0.0",
                port=8000, reload=True, workers=2)


if __name__ == "__main__":
    run()
