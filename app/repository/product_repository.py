from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:

    def get(self, db: Session, id: int): 
        return db.get (Product, id)

    
    def get_all(self, db:Session):
        return db.query(Product).all()

    def get_by_category(self, db: Session, category_id: int): 
        products= db.query(Product).filter(Product.category_id == category_id).all()
        return products

    def create(self, db:Session, data: dict): 
        product = Product(**data) 
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def update(self, db: Session, db_obj: Product, data: dict): 
        for field, value in data.items():
            setattr(db_obj, field, value) 
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    
    def delete(self, db:Session, db_obj: Product): 
        db.delete(db_obj)
        db.commit()

product_repository=ProductRepository()