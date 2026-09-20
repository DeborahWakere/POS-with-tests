import os

os.environ["DATABASE_URL"] = "sqlite://"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app
from app.core.security import create_access_token, hashed_password
from app.models.category import Category
from app.models.customer import Customer
from app.models.product import Product
from app.models.supplier import Supplier
from app.models.user import User
from app.models.sale import Sale
from app.models.payment import Payment
from app.models.inventory import Inventory
from app.models.receipt import Receipt
from app.models.saleitem import SaleItem

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Enable SQLite foreign-key enforcement so relational failures behave like the
# PostgreSQL development database.
@event.listens_for(engine, "connect")
def _enable_sqlite_foreign_keys(dbapi_connection, _connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

TestSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        session = TestSessionLocal()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def test_user(db):
    user = User(
        username="testuser",
        password_hash=hashed_password("testpassword123"),
        user_role="cashier",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture
def auth_headers(test_user):
    token = create_access_token(test_user.user_id)
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def category(db):
    obj = Category(category_name="Drinks")
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@pytest.fixture
def supplier(db):
    obj = Supplier(
        supplier_name="Test Supplier",
        contact_person="Test Person",
        contact_number="123456789",
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@pytest.fixture
def customer(db):
    obj = Customer(
        first_name="John",
        last_name="Doe",
        phone_number="0712345678",
        loyalty_points=10,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@pytest.fixture
def product(db, category, supplier):
    obj = Product(
        name="Coca Cola",
        sku="SKU-001",
        price=100,
        cost=60,
        category_id=category.category_id,
        supplier_id=supplier.supplier_id,
        is_active=True,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@pytest.fixture
def sale(db, test_user, customer):
    obj = Sale(
        total_amount=200,
        user_id=test_user.user_id,
        customer_id=customer.customer_id,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@pytest.fixture
def payment(db, sale):
    obj = Payment(
        payment_method="cash",
        amount_paid=200,
        sale_id=sale.sale_id,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@pytest.fixture
def inventory(db, product):
    obj = Inventory(
        product_id=product.id,
        quantity=25,
        location="Main Store",
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@pytest.fixture
def receipt(db, sale, payment, customer):
    obj = Receipt(
        receipt_barcode=100001,
        sale_id=sale.sale_id,
        payment_id=payment.payment_id,
        customer_id=customer.customer_id,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@pytest.fixture
def sale_item(db, sale, product):
    obj = SaleItem(
        quality=2,
        unit_price=100,
        sale_id=sale.sale_id,
        product_id=product.id,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
