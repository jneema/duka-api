from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SalesBase(BaseModel):
    quantity: int
    created_at: datetime
    completed: bool


class ProductBase(BaseModel):
    name: str
    bp: int
    sp: int
    serial_no: int

class ProductCreate(ProductBase):
    pass
class ProductPut(BaseModel):
    name: Optional[str]
    bp: Optional[int]       
    sp: Optional[int]   
    serial_no: Optional[int]   

    class Config:
        orm_mode = True 

class ProductInfo(ProductBase):
    id: int
    created: datetime  

    class Config:
        orm_mode = True

class ProductInDB(ProductBase):
    id : int
    created: datetime
    # todos: List[SalesBase]

    class Config:
        orm_mode = True


class SalesInDB(SalesBase):
    id : int
    created: datetime
    completed: bool
    product: ProductInfo        