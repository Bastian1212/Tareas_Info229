from typing import List, Optional

from pydantic import BaseModel


class  categoryBase(BaseModel):
  value: str

class categoryCreate(categoryBase):
  pass


class category(categoryBase):


  id : int 
  newTitle: str
  class Config:
    orm_mode = True 


class newBase(BaseModel):

  title : str
  date : str
  url : str
  media_outlet :str

class newCreate(newBase):
  pass

class new(newBase):

  id : int 

  categorys : List[category] = []

  class Config:

    orm_model = True





