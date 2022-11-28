from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Generator
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

# models
from app.models.products import Products as ProductsModel

# schema
from app.schema import ProductBase, ProductCreate, ProductPut, ProductInfo, ProductInDB


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()   

product_router = APIRouter()

# get all products
@product_router.get("/products",
response_model=List[ProductInfo],
summary="all products",
status_code=200)
def get_products(db: Session = Depends(get_db)):
    return db.query(ProductsModel).all()

# get single product
@product_router.get("/{productID}",
response_model=ProductInfo,
summary="single product",
status_code=200)
def get_product(productID:int, db: Session = Depends(get_db)):
    # check if product exists
    product = db.query(ProductsModel).filter_by(id=productID).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product does not exist")
    
    return db.query(ProductsModel).get(productID)


#  add new product
@product_router.post("/products",
response_model=ProductInDB,
summary="add a product",
status_code=201,
)
def add_product(payload: ProductCreate,db: Session = Depends(get_db) ):
    # check if product exists
    serial_no = db.query(ProductsModel).filter(ProductsModel.serial_no == payload.serial_no).first()

    if serial_no:
        raise HTTPException(status_code=400, detail= f"{payload.serial_no} is already taken")
    res: ProductInfo = ProductsModel(name = payload.name, bp = payload.bp, sp = payload.sp, serial_no = payload.serial_no)
    db.add(res)
    db.commit()
    return res
# make changes to the product details
@product_router.put("/{productID}",
response_model=ProductPut,
summary="update a user item",
status_code=200,
)
def edit_product(productID:int, payload:ProductPut, db: Session = Depends(get_db) ):
    # check if id exists
    product = db.query(ProductsModel).filter_by(id=productID).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product does not exist")
    # update user details
    res: ProductPut = ProductsModel(name = payload.name, bp = payload.bp, sp = payload.sp, serial_no = payload.serial_no)
    db.add(res)
    db.add(res)
    db.commit()

    return res

# Delete product
@product_router.delete("/{productID}",
response_model= Dict[str,str],
summary="delete an item",
status_code=200,
)
def delete_product(productID:int, db: Session = Depends(get_db) ):
    # check if id exists
    product = db.query(ProductsModel).filter_by(id=productID).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product does not exist")
        # delete user details
    else:
        db.delete(product)    
        db.commit()
    return {"message": "Product deleted successfully"}
