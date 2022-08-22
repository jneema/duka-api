from sqlalchemy import Column, Integer, ForeignKey, Boolean, datetime, DateTime
from db.base_class import Base
from sqlalchemy.orm import relationship

class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, autoincrement = True, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), autoincrement = True)
    quantity = Column(Integer, unique=False)
    created_at = Column(DateTime, nullable = False, default = datetime.utcnow)
    completed = Column(Boolean, default=False)

    product = relationship("Products", back_populates='sales')