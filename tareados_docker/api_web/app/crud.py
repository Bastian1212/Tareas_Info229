from sqlalchemy.orm import Session

from . import models, schemas



def get_new(db: Session, user_id: int):
    return db.query(models.new).filter(models.new.id == models.id2).first()


def get_new_by_title(db: Session, titles: str):
    return db.query(models.new).filter(models.new.title == models.title).first()


def get_news(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.new).offset(skip).limit(limit).all()



def create_new(db: Session, new: schemas.newCreate):
    
    db_new = models.new(title = new.title, date = new.date, url = new.url, media_outlet = new.media_outlet )


    db.add(db_new)
    db.commit()
    db.refresh(db_new)
    return db_new