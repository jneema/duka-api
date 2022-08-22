from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# )Orms's handle to the database is the session and it helps to start talking to our database

engine = create_engine("postgresql://postgres:nyanumba@localhost:5433/duka-api")

SessionLocal = sessionmaker(bind=engine,
autocommit=False, autoflush=False)

conn = SessionLocal()
