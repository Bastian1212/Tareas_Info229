from sqlalchemy.orm import Session

import models, schemas


#####  OK ##############################
def get_new(db: Session, new_id: int):
    return db.query(models.new).filter(models.new.id == new_id).first()

def get_new_by_title(db: Session, titles: str):
    return db.query(models.new).filter(models.new.title == titles).first()

def get_news(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.new).offset(skip).limit(limit).all()



def create_new(db: Session, new: schemas.newCreate):
    
    db_new = models.new(title = new.title, date = new.date, url = new.url, media_outlet = new.media_outlet )


    db.add(db_new)
    db.commit()
    db.refresh(db_new)
    return db_new



def get_categorys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.category).offset(skip).limit(limit).all()