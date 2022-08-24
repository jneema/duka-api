from sys import prefix
from fastapi import APIRouter
from .products import product_router
from .sales import sales_router

router = APIRouter()

router.include_router(product_router, prefix="/products", tags=['PRODUCTS'])
router.include_router(sales_router, prefix="/sales", tags=['SALES'])