from sqlalchemy.orm import Session

from app.models.saleitem import SaleItem


class SaleItemRepository:

    def get(self, db: Session, sale_item_id: int):
        return db.get(SaleItem, sale_item_id)

    def get_all(self, db: Session):
        return db.query(SaleItem).all()

    def get_by_sale(self, db: Session, sale_id: int):
        return db.query(SaleItem).filter(
            SaleItem.sale_id == sale_id
        ).all()

    def get_by_product(self, db: Session, product_id: int):
        return db.query(SaleItem).filter(
            SaleItem.product_id == product_id
        ).all()

    def create(self, db: Session, data: dict):
        saleitem = SaleItem(**data)

        db.add(saleitem)
        db.commit()
        db.refresh(saleitem)

        return saleitem

    def update(self, db: Session, db_obj: SaleItem, data: dict):
        for field, value in data.items():
            setattr(db_obj, field, value)

        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, db: Session, db_obj: SaleItem):
        db.delete(db_obj)
        db.commit()

        return db_obj


saleitem_repository = SaleItemRepository()