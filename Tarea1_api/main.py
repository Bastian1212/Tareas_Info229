from typing import List
from datetime  import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session



import crud, models, schemas
from database import SessionLocal, engine

from datetime import datetime







def databaseC():

    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)

    database = SessionLocal()

    database.add(models.new(title = 'noticia ', date = '20/06/2020', url = 'www.noticia.cl', media_outlet = 'Medio'))
    database.add(models.new(title = 'noticia2 ', date = '11/12/2021', url = 'www.noticia_2.cl', media_outlet = 'Medio2'))

    database.add(models.category(category = 'Cientificas', newTitle = 'noticia'))
    database.add(models.category(category = 'Deportivas', newTitle = 'noticia2'))

    database.commit()





##databaseC()
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/news/", response_model=schemas.new)
def create_new(neww: schemas.newCreate, db: Session = Depends(get_db)):
    db_new = crud.get_user_by_title(db, title=models.new.title)
    if db_new:
        raise HTTPException(status_code=400, detail="Titulo  already registered")
    return crud.create_user(db=db, neww=models.new)

@app.get("/news/", response_model=List[schemas.new])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_users(db, skip=skip, limit=limit)
    return news

@app.get("/news/{new_id}", response_model=schemas.new)
def read_new(new_id: int, db: Session = Depends(get_db)):
    db_neww = crud.get_new(db, new_id=new_id)
    if db_neww is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_neww



@app.get("/category/", response_model=List[schemas.category])
def read_categorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    category = crud.get_category(db, skip=skip, limit=limit)
    return category

