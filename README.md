# POS FastAPI Backend

## Project structure

The backend contains ten main entities:

- Category
- Customer
- Inventory
- Payment
- Product
- Receipt
- Sale
- SaleItem
- Supplier
- User

Each entity has its own test module under `tests/`, with CRUD, validation, missing-resource, and relevant failure/security scenarios.

## Run the API

Create and activate a virtual environment, then install the application dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the API from the repository root:

```bash
uvicorn app.main:app --reload
```

## Run the automated tests

The tests use an isolated in-memory SQLite database. They do **not** connect to the normal PostgreSQL development database.

Install the test dependencies:

```bash
pip install -r requirements-test.txt
```

Run the complete suite:

```bash
python -m pytest -q
```

The suite currently contains **88 tests** covering all ten entities, database configuration, the main application, and security.

### Test files

```text
tests/
├── conftest.py
├── test_database.py
├── test_main.py
├── test_security.py
├── test_category.py
├── test_customer.py
├── test_inventory.py
├── test_payment.py
├── test_product.py
├── test_receipt.py
├── test_sale.py
├── test_saleitem.py
├── test_supplier.py
└── test_user.py
```

## GitHub Actions

`.github/workflows/tests.yml` runs automatically on every push and every pull request. It:

1. Checks out the repository.
2. Sets up Python.
3. Installs the test dependencies.
4. Runs the complete Pytest suite against SQLite.
5. Fails the workflow if any test fails.

No PostgreSQL server or Heroku deployment is required for the automated tests.
