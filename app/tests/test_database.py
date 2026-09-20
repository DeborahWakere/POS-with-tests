"""Tests for database configuration and test-database isolation."""

from sqlalchemy import inspect
from app.database import Base, engine, get_db

from app import models


def test_database_engine_uses_sqlite_for_tests():
    assert engine.url.get_backend_name() == "sqlite"


def test_database_engine_uses_isolated_in_memory_database():
    assert engine.url.database in (None, "")


def test_all_entity_tables_are_registered():
    expected_tables = {
        "categories",
        "customers",
        "inventory",
        "payments",
        "products",
        "receipts",
        "sales",
        "saleitems",
        "suppliers",
        "users",
    }
    assert expected_tables.issubset(set(Base.metadata.tables))


def test_database_session_generator_opens_and_closes():
    db = next(get_db())
    try:
        assert db.is_active
    finally:
        db.close()


def test_sqlite_tables_can_be_created_and_inspected(db):
    inspector = inspect(db.bind)
    table_names = set(inspector.get_table_names())
    assert {
        "categories",
        "customers",
        "inventory",
        "payments",
        "products",
        "receipts",
        "sales",
        "saleitems",
        "suppliers",
        "users",
    }.issubset(table_names)
