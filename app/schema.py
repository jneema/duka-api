from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
class ProductBase(BaseModel):
    name: str
    bp: int
    sp: int
    serial_no: int

class ProductCreate(ProductBase):
    pass

class ProductPut(BaseModel):
    id: Optional[int]
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


class SalesBase(BaseModel):
    quantity: int
    product_id: int


class SalesInDB(SalesBase):
    id : int
    created_at: datetime

    class Config:
        orm_mode = True
  

class SalesInfo(BaseModel):
    id: Optional[int]
    Name: Optional[str]
    Quantity: Optional[int]
    Profit: Optional[int]

    class Config:
        orm_mode = True    

class SalesCreate(SalesBase):
    pass        