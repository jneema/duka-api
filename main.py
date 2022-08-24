from typing import Union, Generator, List, Dict
from endpoints.api import router

from fastapi import Depends, FastAPI

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()    

app = FastAPI(
    title="Duka API",
    summary="A simple duka api",
    version="0.1.0",
    docs_url="/developer/docs",
    redoc_url="/developer/redoc",
    contact={
        "name": "Joy",
        "email":"joeyshem33@gmail.com"
    }
)

# models
from models.products import Products

# db config
from db.base_class import Base
from db.session import engine, SessionLocal

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(router, responses={
                       200: {'description': 'Ok'},
                       201: {'description': 'Created'},
                       202: {'description': 'Accepted'},
                       400: {"description": "Bad Request"},
                       401: {"description": "Unauthorized"},
                       403: {"description": "Forbidden"},
                       404: {"description": "Not found"},
                       405: {"description": "Method not allowed"}
                        }
)    
