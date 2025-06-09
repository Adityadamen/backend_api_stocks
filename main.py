from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from stocks.router import stock_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:1234"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stock_router, prefix="/api/stocks")

@app.get("/")
def root():
    return {"message": "Welcome to Stock API"}
