from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def get(self, db: Session, user_id: int): return db.get(User, user_id)
    def get_by_username(self, db: Session, username: str): return db.query(User).filter(User.username == username).first()
    def get_all(self, db: Session): return db.query(User).all()
    def create(self, db: Session, data: dict):
        user = User(**data); db.add(user); db.commit(); db.refresh(user); return user
    def update(self, db: Session, db_obj: User, data: dict):
        for field, value in data.items(): setattr(db_obj, field, value)
        db.commit(); db.refresh(db_obj); return db_obj
    def delete(self, db: Session, db_obj: User): db.delete(db_obj); db.commit(); return db_obj
user_repository = UserRepository()
