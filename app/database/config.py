"""
Database configuration for the Risk Control API Platform.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///./risk_control.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


Base = declarative_base()

def get_db():
    """
    Provide a database session for each API request
    and ensure the session is closed afterward.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()