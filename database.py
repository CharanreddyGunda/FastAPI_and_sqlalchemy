from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()