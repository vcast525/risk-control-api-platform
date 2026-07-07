"""
Database configuration for the Risk Control API Platform.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL environment variable is not set.")


engine = create_engine(DATABASE_URL)


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