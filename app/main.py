import uvicorn
from fastapi import FastAPI

from routers import price_estimation

app = FastAPI(
    title="Real Estate Valuation",
    version='0.0.1'
)

app.include_router(price_estimation)


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)
