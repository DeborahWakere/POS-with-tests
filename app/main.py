from fastapi import FastAPI
from app.routers import (
    product,
    sale,
    user,
    category,
    payment,
    inventory,
    receipt,
    saleitem,
    customer,
    supplier,
)
from app.database import engine, Base, get_db
from app.models import (
    product as product_model,
    sale as sale_model,
    user as user_model,
    category as category_model,
    customer as customer_model,
    payment as payment_model,
    inventory as inventory_model,
    receipt as receipt_model,
    saleitem as saleitem_model,
)


Base.metadata.create_all(bind=engine)

app = FastAPI(title="POS API", version="1")

app.include_router(product.router)
app.include_router(sale.router)
app.include_router(user.router)
app.include_router(category.router)
app.include_router(customer.router)
app.include_router(payment.router)
app.include_router(inventory.router)
app.include_router(receipt.router)
app.include_router(supplier.router)
app.include_router(saleitem.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Point of Sale API."}
