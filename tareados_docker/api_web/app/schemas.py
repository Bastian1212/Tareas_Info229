from typing import List, Optional

from pydantic import BaseModel


class  has_categoryBase(BaseModel):
  value: str

class has_categoryCreate(has_categoryBase):
  pass


class has_category(has_categoryBase):


  id : int 
  id2 : int
  class Config:
    orm_mode = True 


class newsBase(BaseModel):

  title : str
  date : str
  url : str
  media_outlet :str

class newsCreate(newsBase):
  pass

class news(newsBase):

  id : int 

  value : List[has_category] = []

  class Config:

    orm_model = True





