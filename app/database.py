import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Use an environment override so tests can use SQLite without requiring PostgreSQL.
database_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/pos_db")

engine_kwargs = {"echo": False, "future": True}
if database_url.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(database_url, **engine_kwargs)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
