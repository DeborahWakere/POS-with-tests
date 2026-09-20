from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.customer import CustomerCreate, CustomerRead, CustomerUpdate
from app.services import customers_services

router= APIRouter( prefix="/customers", tags=["customers"])

@router.get("/", response_model=list[CustomerRead])
def  listcustomers(db:Session = Depends(get_db)):
    return customers_services.list_customers(db)
            
@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(customer_id:int, db:Session = Depends(get_db)): 
    return customers_services.get_customer(db, customer_id)

@router.post("/", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
def create_customer(data:CustomerCreate, db:Session = Depends(get_db)): 
    return customers_services.create_customer(db, data)

@router.put("/{customer_id}", response_model=CustomerRead)
def update_customer(
    customer_id:int, data:CustomerUpdate, db:Session = Depends(get_db)): 
    return customers_services.update_customer(db, customer_id, data)

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id:int, db:Session = Depends(get_db)):
    return customers_services.delete_customer(db, customer_id)