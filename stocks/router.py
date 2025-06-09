# stocks/router.py

from fastapi import APIRouter
from .utils import get_stock_data

stock_router = APIRouter()

@stock_router.get("/data")
def fetch_data():
    return get_stock_data()
