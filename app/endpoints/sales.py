from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Generator
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.products import Products
from app.models.sales import Sales
from sqlalchemy import func


from app.models.sales import Sales as SalesModel

from app.schema import SalesBase, SalesInDB, SalesInfo, SalesCreate


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()   

sales_router = APIRouter()

# get all sales
@sales_router.get("/sales",
response_model=List[SalesInfo],
summary="all sales",
status_code=200)
def get_sales(db: Session = Depends(get_db)):
    # return db.query(SalesModel).all()
    sales= db.query(Sales.id, Products.name, func.sum(Sales.quantity).label("Quantity"), func.sum((Products.sp-Products.bp)*Sales.quantity).label("Profit")).join(Sales, Products.id == Sales.product_id).group_by(Products.name, Products.id, Sales.id).order_by(Sales.id).all()
    for sale in sales:
        print('id:', sale[0], 'Name:', sale[1], 'Quantity:', sale[2], 'Profit:', sale[3])
    return sales

# get single sale
@sales_router.get('/{saleID}',
response_model=SalesInfo,
summary="single sale",
status_code=200)
def get_sale(saleID:int, db: Session = Depends(get_db)):

    sale = db.query(Sales.id, Products.name, func.sum(Sales.quantity).label("Quantity"), func.sum((Products.sp-Products.bp)*Sales.quantity).label("Profit")).join(Sales, Products.id == Sales.product_id).group_by(Products.name, Products.id, Sales.id).filter(SalesModel.id == saleID).first()
    # for x in sale:
    #     print('id:', x[0], 'Name:', x[1], 'Quantity:', x[2], 'Profit:', x[3])

    return sale 
#  add new sales
@sales_router.post("/sales",
response_model=SalesInDB,
summary="add a sale",
status_code=201,
)
def add_sale(payload: SalesCreate,db: Session = Depends(get_db) ):
    # check if sale exists
    product = db.query(SalesModel).filter(SalesModel.product_id == payload.product_id).first()

    if product:
        raise HTTPException(status_code=400, detail= f"{payload.product_id} is already taken")
    res: SalesInfo = SalesModel(quantity = payload.quantity, created_at = datetime.utcnow(), product_id = payload.product_id)
    db.add(res)
    db.commit()
    return res    
