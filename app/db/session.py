from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# )Orms's handle to the database is the session and it helps to start talking to our database

engine = create_engine("postgresql://postgres:12345@localhost:5432/api")

SessionLocal = sessionmaker(bind=engine,
autocommit=False, autoflush=False)

conn = SessionLocal()

