from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# )Orms's handle to the database is the session and it helps to start talking to our database

engine = create_engine("postgresql://upuirxveufqnwh:6e96d1ba907415f41cf9727721662ee58928346a7f1907beaf7af0e7072647d2@ec2-34-248-169-69.eu-west-1.compute.amazonaws.com:5432/dao165b16hpbgt")

SessionLocal = sessionmaker(bind=engine,
autocommit=False, autoflush=False)

conn = SessionLocal()
