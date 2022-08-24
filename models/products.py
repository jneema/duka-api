from sqlalchemy import Column, Numeric, Integer, String, Boolean, DateTime, func
from db.base_class import Base
from sqlalchemy.orm import relationship

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement = True, nullable=False)
    name = Column(String(80), unique=True)
    bp = Column(Numeric(15), unique=False)
    sp = Column(Numeric(15), unique=False)
    serial_no = Column(Integer, unique=False)
    completed = Column(Boolean, default=False)
    created = Column(DateTime(timezone=True),server_default=func.now())


    sales = relationship("Sales", back_populates = 'products')