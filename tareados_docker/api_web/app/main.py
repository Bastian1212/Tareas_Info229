from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine



app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/news/", response_model=schemas.new)
def create_new(user: schemas.newsCreate, db: Session = Depends(get_db)):
    db_new = crud.get_user_by_title(db, title=models.new.title)
    if db_new:
        raise HTTPException(status_code=400, detail="Titulo  already registered")
    return crud.create_user(db=db, new=models.new)

@app.get("/news/", response_model=List[schemas.new])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_users(db, skip=skip, limit=limit)
    return news

@app.get("/news/{new_id}", response_model=schemas.new)
def read_new(new_id: int, db: Session = Depends(get_db)):
    db_new = crud.get_new(db, new_id=new_id)
    if db_new is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_new


@app.post("/news/{news_id}/value/", response_model=schemas.value)
def create_item_for_new(
    new_id: int, value: schemas.has_categoryCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, has_category=models.has_categoryCreate, new_id=new_id)


@app.get("/category/", response_model=List[schemas.has_category])
def read_categorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return models.category

