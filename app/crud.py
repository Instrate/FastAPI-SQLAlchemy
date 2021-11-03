from sqlalchemy.orm import Session 
import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).one()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'notreallyhashed'
    db_user = models.User(username = user.username, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).one()
    db.delete(db_user)
    db.commit()
    return db_user
    # print(f'\n{db_user=}\n')
    # if(db_user):
    #     return False
    # return True

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user_items(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item